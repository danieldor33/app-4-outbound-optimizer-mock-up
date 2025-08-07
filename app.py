import streamlit as st
import pandas as pd
from datetime import datetime
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode

# --- 1. Sample Data with 7 accounts and contacts ---
def load_sample_data():
    accounts = pd.DataFrame([
        # Original 2 accounts
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
        {
            "Country": "UK",
            "Account Name": "Globex Ltd.",
            "Parent Company Domain": "globex.com",
            "Website": "www.globex.com",
            "Is Previous Churned Account?": True,
            "Number Of Contacts": 1,
            "Contacts Activity Score": 54,
            "Contacts With Trials": 0,
            "Number Of Past Opps": 1,
            "Last Contact Event Date": "2025-07-30",
            "Last Contact Event Description": "Meeting",
            "Last Rep Event Date": "2025-07-31",
            "Last Rep Event Description": "LinkedIn Message",
            "Industry": "Finance",
            "Industry Sub-Type": "Banking"
        },
        # 5 additional accounts
        {
            "Country": "Canada",
            "Account Name": "MapleSoft",
            "Parent Company Domain": "maplesoft.ca",
            "Website": "www.maplesoft.ca",
            "Is Previous Churned Account?": False,
            "Number Of Contacts": 2,
            "Contacts Activity Score": 76,
            "Contacts With Trials": 1,
            "Number Of Past Opps": 2,
            "Last Contact Event Date": "2025-07-28",
            "Last Contact Event Description": "Call",
            "Last Rep Event Date": "2025-07-29",
            "Last Rep Event Description": "Email",
            "Industry": "Education",
            "Industry Sub-Type": "EdTech"
        },
        {
            "Country": "Germany",
            "Account Name": "TechHaus GmbH",
            "Parent Company Domain": "techhaus.de",
            "Website": "www.techhaus.de",
            "Is Previous Churned Account?": False,
            "Number Of Contacts": 2,
            "Contacts Activity Score": 92,
            "Contacts With Trials": 2,
            "Number Of Past Opps": 4,
            "Last Contact Event Date": "2025-08-03",
            "Last Contact Event Description": "Meeting",
            "Last Rep Event Date": "2025-08-04",
            "Last Rep Event Description": "Call",
            "Industry": "Manufacturing",
            "Industry Sub-Type": "Electronics"
        },
        {
            "Country": "Australia",
            "Account Name": "Koala Tech",
            "Parent Company Domain": "koalatech.au",
            "Website": "www.koalatech.au",
            "Is Previous Churned Account?": True,
            "Number Of Contacts": 2,
            "Contacts Activity Score": 63,
            "Contacts With Trials": 0,
            "Number Of Past Opps": 1,
            "Last Contact Event Date": "2025-07-27",
            "Last Contact Event Description": "LinkedIn Message",
            "Last Rep Event Date": "2025-07-28",
            "Last Rep Event Description": "Call",
            "Industry": "Retail",
            "Industry Sub-Type": "E-commerce"
        },
        {
            "Country": "India",
            "Account Name": "Bharat Systems",
            "Parent Company Domain": "bharatsystems.in",
            "Website": "www.bharatsystems.in",
            "Is Previous Churned Account?": False,
            "Number Of Contacts": 2,
            "Contacts Activity Score": 81,
            "Contacts With Trials": 1,
            "Number Of Past Opps": 3,
            "Last Contact Event Date": "2025-08-05",
            "Last Contact Event Description": "Email",
            "Last Rep Event Date": "2025-08-06",
            "Last Rep Event Description": "Meeting",
            "Industry": "IT Services",
            "Industry Sub-Type": "Consulting"
        },
        {
            "Country": "France",
            "Account Name": "Paris Innovations",
            "Parent Company Domain": "parisinnov.fr",
            "Website": "www.parisinnov.fr",
            "Is Previous Churned Account?": False,
            "Number Of Contacts": 2,
            "Contacts Activity Score": 70,
            "Contacts With Trials": 0,
            "Number Of Past Opps": 2,
            "Last Contact Event Date": "2025-07-26",
            "Last Contact Event Description": "Call",
            "Last Rep Event Date": "2025-07-27",
            "Last Rep Event Description": "LinkedIn Message",
            "Industry": "Media",
            "Industry Sub-Type": "Digital Publishing"
        }
    ])

    contacts = pd.DataFrame([
        # Original contacts
        {"First Name": "John", "Last Name": "Doe", "Country": "USA", "Domain": "acme.com", "Email": "john.doe@acme.com", "Phone": "+1 555 123 4567", "Last Action Date": "2025-08-01", "Last Action Type Event": "Email", "Last LinkedIn Connect Submission Date": "", "Last LinkedIn Message Submission Date": "", "Last Email Submission Date": "2025-08-01", "Last Call Date": "", "Last Meeting Date": ""},
        {"First Name": "Jane", "Last Name": "Smith", "Country": "USA", "Domain": "acme.com", "Email": "jane.smith@acme.com", "Phone": "+1 555 987 6543", "Last Action Date": "", "Last Action Type Event": "", "Last LinkedIn Connect Submission Date": "", "Last LinkedIn Message Submission Date": "", "Last Email Submission Date": "", "Last Call Date": "", "Last Meeting Date": ""},
        {"First Name": "Tom", "Last Name": "Brown", "Country": "UK", "Domain": "globex.com", "Email": "tom.brown@globex.com", "Phone": "+44 20 7946 0958", "Last Action Date": "2025-07-30", "Last Action Type Event": "Meeting", "Last LinkedIn Connect Submission Date": "", "Last LinkedIn Message Submission Date": "", "Last Email Submission Date": "", "Last Call Date": "", "Last Meeting Date": "2025-07-30"},
        # Contacts for MapleSoft
        {"First Name": "Alice", "Last Name": "Johnson", "Country": "Canada", "Domain": "maplesoft.ca", "Email": "alice.j@maplesoft.ca", "Phone": "+1 416 555 1010", "Last Action Date": "", "Last Action Type Event": "", "Last LinkedIn Connect Submission Date": "", "Last LinkedIn Message Submission Date": "", "Last Email Submission Date": "", "Last Call Date": "", "Last Meeting Date": ""},
        {"First Name": "Bob", "Last Name": "Lee", "Country": "Canada", "Domain": "maplesoft.ca", "Email": "bob.lee@maplesoft.ca", "Phone": "+1 416 555 2020", "Last Action Date": "", "Last Action Type Event": "", "Last LinkedIn Connect Submission Date": "", "Last LinkedIn Message Submission Date": "", "Last Email Submission Date": "", "Last Call Date": "", "Last Meeting Date": ""},
        # Contacts for TechHaus
        {"First Name": "Eva", "Last Name": "Müller", "Country": "Germany", "Domain": "techhaus.de", "Email": "eva.mueller@techhaus.de", "Phone": "+49 30 123456", "Last Action Date": "", "Last Action Type Event": "", "Last LinkedIn Connect Submission Date": "", "Last LinkedIn Message Submission Date": "", "Last Email Submission Date": "", "Last Call Date": "", "Last Meeting Date": ""},
        {"First Name": "Lars", "Last Name": "Schmidt", "Country": "Germany", "Domain": "techhaus.de", "Email": "lars.schmidt@techhaus.de", "Phone": "+49 30 654321", "Last Action Date": "", "Last Action Type Event": "", "Last LinkedIn Connect Submission Date": "", "Last LinkedIn Message Submission Date": "", "Last Email Submission Date": "", "Last Call Date": "", "Last Meeting Date": ""},
        # Contacts for Koala Tech
        {"First Name": "Chloe", "Last Name": "Nguyen", "Country": "Australia", "Domain": "koalatech.au", "Email": "chloe.nguyen@koalatech.au", "Phone": "+61 2 1234 5678", "Last Action Date": "", "Last Action Type Event": "", "Last LinkedIn Connect Submission Date": "", "Last LinkedIn Message Submission Date": "", "Last Email Submission Date": "", "Last Call Date": "", "Last Meeting Date": ""},
        {"First Name": "Liam", "Last Name": "Taylor", "Country": "Australia", "Domain": "koalatech.au", "Email": "liam.taylor@koalatech.au", "Phone": "+61 2 8765 4321", "Last Action Date": "", "Last Action Type Event": "", "Last LinkedIn Connect Submission Date": "", "Last LinkedIn Message Submission Date": "", "Last Email Submission Date": "", "Last Call Date": "", "Last Meeting Date": ""},
        # Contacts for Bharat Systems
        {"First Name": "Anjali", "Last Name": "Verma", "Country": "India", "Domain": "bharatsystems.in", "Email": "anjali.verma@bharatsystems.in", "Phone": "+91 22 1234 5678", "Last Action Date": "", "Last Action Type Event": "", "Last LinkedIn Connect Submission Date": "", "Last LinkedIn Message Submission Date": "", "Last Email Submission Date": "", "Last Call Date": "", "Last Meeting Date": ""},
        {"First Name": "Raj", "Last Name": "Kapoor", "Country": "India", "Domain": "bharatsystems.in", "Email": "raj.kapoor@bharatsystems.in", "Phone": "+91 22 8765 4321", "Last Action Date": "", "Last Action Type Event": "", "Last LinkedIn Connect Submission Date": "", "Last LinkedIn Message Submission Date": "", "Last Email Submission Date": "", "Last Call Date": "", "Last Meeting Date": ""},
        # Contacts for Paris Innovations
        {"First Name": "Claire", "Last Name": "Dubois", "Country": "France", "Domain": "parisinnov.fr", "Email": "claire.dubois@parisinnov.fr", "Phone": "+33 1 2345 6789", "Last Action Date": "", "Last Action Type Event": "", "Last LinkedIn Connect Submission Date": "", "Last LinkedIn Message Submission Date": "", "Last Email Submission Date": "", "Last Call Date": "", "Last Meeting Date": ""},
        {"First Name": "Antoine", "Last Name": "Moreau", "Country": "France", "Domain": "parisinnov.fr", "Email": "antoine.moreau@parisinnov.fr", "Phone": "+33 1 9876 5432", "Last Action Date": "", "Last Action Type Event": "", "Last LinkedIn Connect Submission Date": "", "Last LinkedIn Message Submission Date": "", "Last Email Submission Date": "", "Last Call Date": "", "Last Meeting Date": ""}
    ])
    return accounts, contacts


# --- Helper function to update account's last contact event date ---
def update_account_last_contact_date(accounts_df, domain, new_date):
    # Convert "Last Contact Event Date" to datetime for comparison
    accounts_df["Last Contact Event Date"] = pd.to_datetime(accounts_df["Last Contact Event Date"])
    # Find index of the account by domain
    idx = accounts_df.index[accounts_df["Parent Company Domain"] == domain]
    if not idx.empty:
        idx = idx[0]
        old_date = accounts_df.at[idx, "Last Contact Event Date"]
        # Update if new_date is newer
        if pd.isnull(old_date) or new_date > old_date:
            accounts_df.at[idx, "Last Contact Event Date"] = new_date


# --- Streamlit page setup ---
st.set_page_config(layout="wide")
st.title("🧭 Seller Prioritization Assistant")

# --- Load data ---
accounts_df, contacts_df = load_sample_data()

# Convert account dates to datetime for sorting
accounts_df["Last Contact Event Date"] = pd.to_datetime(accounts_df["Last Contact Event Date"], errors='coerce')

# --- Sort accounts by oldest last contact event date (ascending) ---
accounts_df = accounts_df.sort_values(by="Last Contact Event Date", ascending=True).reset_index(drop=True)

# --- AgGrid options for accounts table ---
gb = GridOptionsBuilder.from_dataframe(accounts_df)
gb.configure_selection("single", use_checkbox=True)
grid_options = gb.build()

# --- Display accounts table with selection ---
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

# if selected_rows is a DataFrame, convert it to list of dicts
if hasattr(selected_rows, "to_dict"):
    selected_rows = selected_rows.to_dict(orient="records")

if selected_rows and len(selected_rows) > 0:
    selected_account = selected_rows[0]
else:
    selected_account = accounts_df.iloc[0].to_dict()

selected_domain = selected_account["Parent Company Domain"]



st.subheader(f"Contacts for {selected_account['Account Name']}")

# Filter contacts for the selected account domain
filtered_contacts_df = contacts_df[contacts_df["Domain"] == selected_domain].reset_index(drop=True)

# --- Initialize session state for update requests ---
if "update_request" not in st.session_state:
    st.session_state.update_request = None

# --- Display contacts with action buttons ---
for idx, row in filtered_contacts_df.iterrows():
    st.markdown(f"### {row['First Name']} {row['Last Name']}")
    st.write(f"📍 {row['Country']} | ✉️ {row['Email']} | 📞 {row['Phone']}")
    last_action_date = row["Last Action Date"] if row["Last Action Date"] else "Never"
    last_action_type = row["Last Action Type Event"] if row["Last Action Type Event"] else "No recent action"
    st.write(f"🕒 Last Action: {last_action_type} on {last_action_date}")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        if st.button("📇 LinkedIn Connect", key=f"connect_{idx}"):
            st.session_state.update_request = (row.name, "LinkedIn Connect submission")
        last_date = row["Last LinkedIn Connect Submission Date"]
        st.caption(f"Last: {last_date if last_date else 'Never'}")
    with col2:
        if st.button("💬 LinkedIn Message", key=f"msg_{idx}"):
            st.session_state.update_request = (row.name, "LinkedIn Message")
        last_date = row["Last LinkedIn Message Submission Date"]
        st.caption(f"Last: {last_date if last_date else 'Never'}")
    with col3:
        if st.button("✉️ Email", key=f"email_{idx}"):
            st.session_state.update_request = (row.name, "Email")
        last_date = row["Last Email Submission Date"]
        st.caption(f"Last: {last_date if last_date else 'Never'}")
    with col4:
        if st.button("📞 Call", key=f"call_{idx}"):
            st.session_state.update_request = (row.name, "Call")
        last_date = row["Last Call Date"]
        st.caption(f"Last: {last_date if last_date else 'Never'}")
    with col5:
        if st.button("📅 Meeting", key=f"meeting_{idx}"):
            st.session_state.update_request = (row.name, "Meeting")
        last_date = row["Last Meeting Date"]
        st.caption(f"Last: {last_date if last_date else 'Never'}")

# --- After buttons rendered, process any update requests ---
if st.session_state.update_request is not None:
    contact_idx, action_type = st.session_state.update_request
    today = datetime.today().date()

    # Update contact row fields according to action type
    if action_type == "LinkedIn Connect submission":
        contacts_df.at[contact_idx, "Last LinkedIn Connect Submission Date"] = today
    elif action_type == "LinkedIn Message":
        contacts_df.at[contact_idx, "Last LinkedIn Message Submission Date"] = today
    elif action_type == "Email":
        contacts_df.at[contact_idx, "Last Email Submission Date"] = today
    elif action_type == "Call":
        contacts_df.at[contact_idx, "Last Call Date"] = today
    elif action_type == "Meeting":
        contacts_df.at[contact_idx, "Last Meeting Date"] = today

    # Update last action date & type for contact
    contacts_df.at[contact_idx, "Last Action Date"] = today
    contacts_df.at[contact_idx, "Last Action Type Event"] = action_type

    # Update the account's "Last Contact Event Date" if newer
    update_account_last_contact_date(accounts_df, selected_domain, pd.to_datetime(today))

    # Clear the update request to avoid loops
    st.session_state.update_request = None

    # Safely rerun the app to refresh the UI with updated data
    st.experimental_rerun()

# --- Show info if no account selected (should not happen because we default to
