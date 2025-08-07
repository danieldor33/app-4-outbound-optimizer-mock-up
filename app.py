import streamlit as st
import pandas as pd
from datetime import datetime
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode

def load_sample_data():
    accounts = pd.DataFrame([
        # ... (your accounts data unchanged; omitted here for brevity) ...
        {
            "Country": "USA",
            "Account Name": "Acme Inc.",
            "Parent Company Domain": "acme.com",
            "Website": "www.acme.com",
            "Is Previous Churned Account?": False,
            "Number Of Contacts": 2,
            "Contacts Activity Score": 87,
            "Contacts With Trials": 1,
            "Number Of Past Opps": 3,
            "Last Contact Event Date": "2025-08-01",
            "Last Contact Event Description": "Email",
            "Last Rep Event Date": "2025-08-02",
            "Last Rep Event Description": "Call",
            "Industry": "Software",
            "Industry Sub-Type": "B2B SaaS"
        },
        # Add other accounts similarly as in your code ...
    ])

    contacts = pd.DataFrame([
        # ... (your contacts data unchanged; omitted here for brevity) ...
        {"First Name": "John", "Last Name": "Doe", "Country": "USA", "Domain": "acme.com", "Email": "john.doe@acme.com", "Phone": "+1 555 123 4567", 
         "Last Action Date": "2025-08-01", "Last Action Type Event": "Email", "Last LinkedIn Connect Submission Date": "", "Last LinkedIn Message Submission Date": "", 
         "Last Email Submission Date": "2025-08-01", "Last Call Date": "", "Last Meeting Date": ""},
        # Add other contacts similarly as in your code ...
    ])
    return accounts, contacts
    
def update_account_last_contact_date(accounts_df, domain, new_date):
    accounts_df["Last Contact Event Date"] = pd.to_datetime(accounts_df["Last Contact Event Date"])
    idx = accounts_df.index[accounts_df["Parent Company Domain"] == domain]
    if not idx.empty:
        idx = idx[0]
        old_date = accounts_df.at[idx, "Last Contact Event Date"]
        if pd.isnull(old_date) or new_date > old_date:
            accounts_df.at[idx, "Last Contact Event Date"] = new_date

st.set_page_config(layout="wide")
st.title("🧭 Seller Prioritization Assistant")

# Load data once, and cache it so it's not reloaded every rerun
@st.cache_data
def load_data_cached():
    return load_sample_data()

accounts_df, contacts_df = load_data_cached()

# Convert Last Contact Event Date to datetime for sorting
accounts_df["Last Contact Event Date"] = pd.to_datetime(accounts_df["Last Contact Event Date"], errors='coerce')
accounts_df = accounts_df.sort_values(by="Last Contact Event Date").reset_index(drop=True)

gb = GridOptionsBuilder.from_dataframe(accounts_df)
gb.configure_selection("single", use_checkbox=True)
grid_options = gb.build()

st.subheader("Accounts Overview")
grid_response = AgGrid(
    accounts_df,
    gridOptions=grid_options,
    update_mode=GridUpdateMode.SELECTION_CHANGED,
    theme="streamlit",
    height=300,
    fit_columns_on_grid_load=True,
)

selected_rows = grid_response["selected_rows"]

# Convert selected_rows if needed
if hasattr(selected_rows, "to_dict"):
    selected_rows = selected_rows.to_dict(orient="records")

if selected_rows and len(selected_rows) > 0:
    selected_account = selected_rows[0]
else:
    selected_account = accounts_df.iloc[0].to_dict()

selected_domain = selected_account["Parent Company Domain"]

st.subheader(f"Contacts for {selected_account['Account Name']}")

# Filter contacts by selected domain
filtered_contacts_df = contacts_df[contacts_df["Domain"] == selected_domain].reset_index(drop=True)

# Initialize session state dict to store contact updates (if not exist)
if "contact_updates" not in st.session_state:
    # Store dict: key = contact idx, value = dict of updated fields
    st.session_state.contact_updates = {}

# Function to get displayed contact info, merging base and session state updates
def get_contact_info(idx, base_df):
    base_row = base_df.iloc[idx].to_dict()
    updates = st.session_state.contact_updates.get(idx, {})
    combined = base_row.copy()
    combined.update(updates)
    return combined

# Show contacts with buttons and last event dates under each button
for idx in filtered_contacts_df.index:
    contact = get_contact_info(idx, filtered_contacts_df)

    st.markdown(f"### {contact['First Name']} {contact['Last Name']}")
    st.write(f"📍 {contact['Country']} | ✉️ {contact['Email']} | 📞 {contact['Phone']}")

    # Show the last action type and date on top
    last_action_type = contact.get("Last Action Type Event") or "No recent action"
    last_action_date = contact.get("Last Action Date") or "Never"
    st.write(f"🕒 Last Action: {last_action_type} on {last_action_date}")

    # Create columns for buttons
    col1, col2, col3, col4, col5 = st.columns(5)
    
    # Button helper: renders button + last event date below it
    def action_button(col, label, action_key, update_field, display_field):
        if col.button(label, key=action_key):
            today = datetime.today().date().isoformat()
            # Save update in session state
            st.session_state.contact_updates.setdefault(idx, {})
            st.session_state.contact_updates[idx][update_field] = today
            # Also update last action fields
            st.session_state.contact_updates[idx]["Last Action Date"] = today
            st.session_state.contact_updates[idx]["Last Action Type Event"] = label
            # Mark update trigger flag to force rerun
            st.session_state.update_triggered = True
        
        # Display last event date below the button, or "-" if missing
        last_date = st.session_state.contact_updates.get(idx, {}).get(display_field, filtered_contacts_df.at[idx, display_field]) or "-"
        col.markdown(f"<small>Last: {last_date}</small>", unsafe_allow_html=True)

    # Show buttons with last event date below each
    action_button(col1, "📇 LinkedIn Connect", f"connect_{idx}", "Last LinkedIn Connect Submission Date", "Last LinkedIn Connect Submission Date")
    action_button(col2, "💬 LinkedIn Message", f"msg_{idx}", "Last LinkedIn Message Submission Date", "Last LinkedIn Message Submission Date")
    action_button(col3, "✉️ Email", f"email_{idx}", "Last Email Submission Date", "Last Email Submission Date")
    action_button(col4, "📞 Call", f"call_{idx}", "Last Call Date", "Last Call Date")
    action_button(col5, "📅 Meeting", f"meeting_{idx}", "Last Meeting Date", "Last Meeting Date")

# After all buttons are rendered, if update_triggered rerun the app to refresh UI
if st.session_state.get("update_triggered", False):
    # Update contacts_df with session_state updates to keep data consistent on rerun
    for idx, updates in st.session_state.contact_updates.items():
        for col, val in updates.items():
            contacts_df.at[idx, col] = val

        # Also update account's last contact event date if needed
        if "Last Action Date" in updates:
            update_account_last_contact_date(accounts_df, selected_domain, pd.to_datetime(updates["Last Action Date"]))

    # Clear the flag
    st.session_state.update_triggered = False
    # Rerun app to reflect changes
    try:
        st.experimental_rerun()
    except Exception:
        pass

if not selected_rows:
    st.info("Select an account from the table above to view contacts.")
