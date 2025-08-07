import streamlit as st
import pandas as pd
from datetime import datetime
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode

@st.cache_data
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
            "Account Name": "Globex Ltd. t",
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
        # Original contacts with added fields
        {
            "First Name": "John",
            "Last Name": "Doe",
            "Country": "USA",
            "Domain": "acme.com",
            "Email": "john.doe@acme.com",
            "Phone": "+1 555 123 4567",
            "Last Action Date": "2025-08-01",
            "Last Action Type Event": "Email",
            "Last LinkedIn Connect Submission Date": "",
            "Last LinkedIn Message Submission Date": "",
            "Last Email Submission Date": "2025-08-01",
            "Last Call Date": "",
            "Last Meeting Date": "",
            "Last Add To Cadence Date": "",
            "Title": "Marketing Manager",
            "Department": "Marketing",
            "Use Case": "Market intelligence and competitor analysis"
        },
        {
            "First Name": "Jane",
            "Last Name": "Smith",
            "Country": "USA",
            "Domain": "acme.com",
            "Email": "jane.smith@acme.com",
            "Phone": "+1 555 987 6543",
            "Last Action Date": "",
            "Last Action Type Event": "",
            "Last LinkedIn Connect Submission Date": "",
            "Last LinkedIn Message Submission Date": "",
            "Last Email Submission Date": "",
            "Last Call Date": "",
            "Last Meeting Date": "",
            "Last Add To Cadence Date": "",
            "Title": "Sales Director",
            "Department": "Sales",
            "Use Case": "Lead generation and sales prospecting"
        },
        {
            "First Name": "Tom",
            "Last Name": "Brown",
            "Country": "UK",
            "Domain": "globex.com",
            "Email": "tom.brown@globex.com",
            "Phone": "+44 20 7946 0958",
            "Last Action Date": "2025-07-30",
            "Last Action Type Event": "Meeting",
            "Last LinkedIn Connect Submission Date": "",
            "Last LinkedIn Message Submission Date": "",
            "Last Email Submission Date": "",
            "Last Call Date": "",
            "Last Meeting Date": "2025-07-30",
            "Last Add To Cadence Date": "",
            "Title": "Product Manager",
            "Department": "Product",
            "Use Case": "Competitive benchmarking for product features"
        },
        # MapleSoft contacts
        {
            "First Name": "Alice",
            "Last Name": "Johnson",
            "Country": "Canada",
            "Domain": "maplesoft.ca",
            "Email": "alice.j@maplesoft.ca",
            "Phone": "+1 416 555 1010",
            "Last Action Date": "",
            "Last Action Type Event": "",
            "Last LinkedIn Connect Submission Date": "",
            "Last LinkedIn Message Submission Date": "",
            "Last Email Submission Date": "",
            "Last Call Date": "",
            "Last Meeting Date": "",
            "Last Add To Cadence Date": "",
            "Title": "Business Analyst",
            "Department": "Business Intelligence",
            "Use Case": "Traffic analysis for strategic decisions"
        },
        {
            "First Name": "Bob",
            "Last Name": "Lee",
            "Country": "Canada",
            "Domain": "maplesoft.ca",
            "Email": "bob.lee@maplesoft.ca",
            "Phone": "+1 416 555 2020",
            "Last Action Date": "",
            "Last Action Type Event": "",
            "Last LinkedIn Connect Submission Date": "",
            "Last LinkedIn Message Submission Date": "",
            "Last Email Submission Date": "",
            "Last Call Date": "",
            "Last Meeting Date": "",
            "Last Add To Cadence Date": "",
            "Title": "Digital Marketing Specialist",
            "Department": "Marketing",
            "Use Case": "Campaign performance monitoring"
        },
        # TechHaus contacts
        {
            "First Name": "Eva",
            "Last Name": "Müller",
            "Country": "Germany",
            "Domain": "techhaus.de",
            "Email": "eva.mueller@techhaus.de",
            "Phone": "+49 30 123456",
            "Last Action Date": "",
            "Last Action Type Event": "",
            "Last LinkedIn Connect Submission Date": "",
            "Last LinkedIn Message Submission Date": "",
            "Last Email Submission Date": "",
            "Last Call Date": "",
            "Last Meeting Date": "",
            "Last Add To Cadence Date": "",
            "Title": "Sales Operations Manager",
            "Department": "Sales",
            "Use Case": "Optimizing sales funnel and lead insights"
        },
        {
            "First Name": "Lars",
            "Last Name": "Schmidt",
            "Country": "Germany",
            "Domain": "techhaus.de",
            "Email": "lars.schmidt@techhaus.de",
            "Phone": "+49 30 654321",
            "Last Action Date": "",
            "Last Action Type Event": "",
            "Last LinkedIn Connect Submission Date": "",
            "Last LinkedIn Message Submission Date": "",
            "Last Email Submission Date": "",
            "Last Call Date": "",
            "Last Meeting Date": "",
            "Last Add To Cadence Date": "",
            "Title": "CEO",
            "Department": "Management",
            "Use Case": "High-level market trends and competitor overview"
        },
        # Koala Tech contacts
        {
            "First Name": "Chloe",
            "Last Name": "Nguyen",
            "Country": "Australia",
            "Domain": "koalatech.au",
            "Email": "chloe.nguyen@koalatech.au",
            "Phone": "+61 2 1234 5678",
            "Last Action Date": "",
            "Last Action Type Event": "",
            "Last LinkedIn Connect Submission Date": "",
            "Last LinkedIn Message Submission Date": "",
            "Last Email Submission Date": "",
            "Last Call Date": "",
            "Last Meeting Date": "",
            "Last Add To Cadence Date": "",
            "Title": "Marketing Analyst",
            "Department": "Marketing",
            "Use Case": "Analyzing competitor marketing campaigns"
        },
        {
            "First Name": "Liam",
            "Last Name": "Taylor",
            "Country": "Australia",
            "Domain": "koalatech.au",
            "Email": "liam.taylor@koalatech.au",
            "Phone": "+61 2 8765 4321",
            "Last Action Date": "",
            "Last Action Type Event": "",
            "Last LinkedIn Connect Submission Date": "",
            "Last LinkedIn Message Submission Date": "",
            "Last Email Submission Date": "",
            "Last Call Date": "",
            "Last Meeting Date": "",
            "Last Add To Cadence Date": "",
            "Title": "Product Owner",
            "Department": "Product",
            "Use Case": "Market share tracking and opportunity identification"
        },
        # Bharat Systems contacts
        {
            "First Name": "Anjali",
            "Last Name": "Verma",
            "Country": "India",
            "Domain": "bharatsystems.in",
            "Email": "anjali.verma@bharatsystems.in",
            "Phone": "+91 22 1234 5678",
            "Last Action Date": "",
            "Last Action Type Event": "",
            "Last LinkedIn Connect Submission Date": "",
            "Last LinkedIn Message Submission Date": "",
            "Last Email Submission Date": "",
            "Last Call Date": "",
            "Last Meeting Date": "",
            "Last Add To Cadence Date": "",
            "Title": "Data Scientist",
            "Department": "Analytics",
            "Use Case": "Website traffic and user behavior insights"
        },
        {
            "First Name": "Raj",
            "Last Name": "Kapoor",
            "Country": "India",
            "Domain": "bharatsystems.in",
            "Email": "raj.kapoor@bharatsystems.in",
            "Phone": "+91 22 8765 4321",
            "Last Action Date": "",
            "Last Action Type Event": "",
            "Last LinkedIn Connect Submission Date": "",
            "Last LinkedIn Message Submission Date": "",
            "Last Email Submission Date": "",
            "Last Call Date": "",
            "Last Meeting Date": "",
            "Last Add To Cadence Date": "",
            "Title": "Business Development Manager",
            "Department": "Sales",
            "Use Case": "Identifying new business opportunities"
        },
        # Paris Innovations contacts
        {
            "First Name": "Claire",
            "Last Name": "Dubois",
            "Country": "France",
            "Domain": "parisinnov.fr",
            "Email": "claire.dubois@parisinnov.fr",
            "Phone": "+33 1 2345 6789",
            "Last Action Date": "",
            "Last Action Type Event": "",
            "Last LinkedIn Connect Submission Date": "",
            "Last LinkedIn Message Submission Date": "",
            "Last Email Submission Date": "",
            "Last Call Date": "",
            "Last Meeting Date": "",
            "Last Add To Cadence Date": "",
            "Title": "Marketing Director",
            "Department": "Marketing",
            "Use Case": "Campaign effectiveness and market reach"
        },
        {
            "First Name": "Antoine",
            "Last Name": "Moreau",
            "Country": "France",
            "Domain": "parisinnov.fr",
            "Email": "antoine.moreau@parisinnov.fr",
            "Phone": "+33 1 9876 5432",
            "Last Action Date": "",
            "Last Action Type Event": "",
            "Last LinkedIn Connect Submission Date": "",
            "Last LinkedIn Message Submission Date": "",
            "Last Email Submission Date": "",
            "Last Call Date": "",
            "Last Meeting Date": "",
            "Last Add To Cadence Date": "",
            "Title": "Product Manager",
            "Department": "Product",
            "Use Case": "Competitive product positioning"
        }
    ])

    return accounts, contacts

accounts_df, contacts_df = load_sample_data()

ACCOUNT_BG_COLOR = "#e6f2ff"  # light blue for account section
CONTACT_BG_COLOR = "#f9f9f9"  # light grey for contacts section

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

def load_data_cached():
    return load_sample_data()

accounts_df, contacts_df = load_data_cached()
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

if "reset_trigger" not in st.session_state:
    st.session_state.reset_trigger = False

if st.button("🔄 Reset All Updates"):
    st.session_state.contact_updates = {}
    st.session_state.contact_move_to_bottom = []
    st.session_state.reset_trigger = True
    st.stop()  # Stop execution, Streamlit will rerun on next interaction

if st.session_state.reset_trigger:
    st.session_state.reset_trigger = False
    # No explicit rerun here, Streamlit naturally reruns after st.stop()

selected_rows = grid_response["selected_rows"]
if hasattr(selected_rows, "to_dict"):
    selected_rows = selected_rows.to_dict(orient="records")

# Initialize session state
if "contact_updates" not in st.session_state:
    st.session_state.contact_updates = {}

if "contact_move_to_bottom" not in st.session_state:
    st.session_state.contact_move_to_bottom = []  # stores emails of contacts to move down

# Helper: color date based on days passed
def color_date(date_str):
    if not date_str or date_str == '—' or pd.isna(date_str):
        return "—"
    try:
        date_obj = pd.to_datetime(date_str).date()
    except Exception:
        return date_str
    days_passed = (datetime.today().date() - date_obj).days
    if days_passed <= 2:
        color = "green"
    elif 3 <= days_passed <= 7:
        color = "orange"
    else:
        color = "red"
    return f'<span style="color:{color}; font-weight:bold;">{date_str}</span>'

def get_contact_info(idx, base_df):
    base_row = base_df.iloc[idx].to_dict()
    # Key by Email for updates
    updates = st.session_state.contact_updates.get(base_row["Email"], {})
    combined = base_row.copy()
    combined.update(updates)
    return combined

if selected_rows and len(selected_rows) > 0:
    selected_account = selected_rows[0]
    selected_domain = selected_account["Parent Company Domain"]
    # Account section with background color
    st.markdown(
        f'<div style="background-color: {ACCOUNT_BG_COLOR}; padding: 15px; border-radius: 5px;">'
        f'<h3>Contacts for {selected_account["Account Name"]}</h3></div>', 
        unsafe_allow_html=True,
    )

    filtered_contacts_df = contacts_df[contacts_df["Domain"] == selected_domain].reset_index(drop=True)

    # Reorder contacts: move those in session_state.contact_move_to_bottom to bottom
    if st.session_state.contact_move_to_bottom:
        bottom_emails = st.session_state.contact_move_to_bottom
        top_df = filtered_contacts_df[~filtered_contacts_df["Email"].isin(bottom_emails)]
        bottom_df = filtered_contacts_df[filtered_contacts_df["Email"].isin(bottom_emails)]
        filtered_contacts_df = pd.concat([top_df, bottom_df], ignore_index=True)
else:
    st.markdown(
    f'<div style="background-color: {ACCOUNT_BG_COLOR}; padding: 15px; border-radius: 5px;">'
    '<h3>All Contacts (No Account Selected)</h3></div>', 
    unsafe_allow_html=True,
    )
    filtered_contacts_df = contacts_df.reset_index(drop=True)

    # Also reorder for no account selected
    if st.session_state.contact_move_to_bottom:
        bottom_emails = st.session_state.contact_move_to_bottom
        top_df = filtered_contacts_df[~filtered_contacts_df["Email"].isin(bottom_emails)]
        bottom_df = filtered_contacts_df[filtered_contacts_df["Email"].isin(bottom_emails)]
        filtered_contacts_df = pd.concat([top_df, bottom_df], ignore_index=True)

for idx in filtered_contacts_df.index:
    contact = get_contact_info(idx, filtered_contacts_df)

    contact_number = idx + 1

    st.markdown(
        f'<div style="background-color: {CONTACT_BG_COLOR}; padding: 10px; margin-bottom: 10px; border-radius: 5px;">'
        f'<h4>{contact_number}. {contact["First Name"]} {contact["Last Name"]}</h4>'
        f'<p>📍 {contact["Country"]} | ✉️ {contact["Email"]} | 📞 {contact["Phone"]} | '
        f'🏷️ {contact.get("Title", "—")} | 🏢 {contact.get("Department", "—")} | '
        f'💡 Use Case: {contact.get("Use Case", "—")}</p>'
        f'</div>',
        unsafe_allow_html=True,
    )
    last_action_type = contact.get('Last Action Type Event') or '—'
    last_action_date = contact.get('Last Action Date') or '—'
    colored_date = color_date(last_action_date)
    st.markdown(f"🕒 Last Action: {last_action_type} on {colored_date}", unsafe_allow_html=True)

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    def action_button(col, label, action_key, update_field, display_field):
        if col.button(label, key=action_key):
            today = datetime.today().date().isoformat()
            email = contact["Email"]
            st.session_state.contact_updates.setdefault(email, {})
            st.session_state.contact_updates[email][update_field] = today
            st.session_state.contact_updates[email]["Last Action Date"] = today
            st.session_state.contact_updates[email]["Last Action Type Event"] = label
            st.session_state.update_triggered = True

            if email not in st.session_state.contact_move_to_bottom:
                st.session_state.contact_move_to_bottom.append(email)

        last_date = (
            st.session_state.contact_updates.get(contact["Email"], {}).get(display_field)
            or filtered_contacts_df.at[idx, display_field]
            or "-"
        )
        col.markdown(f"<small>Last: {last_date}</small>", unsafe_allow_html=True)

    action_button(col1, "📇 LinkedIn Connect", f"connect_{idx}", "Last LinkedIn Connect Submission Date", "Last LinkedIn Connect Submission Date")
    action_button(col2, "💬 LinkedIn Message", f"msg_{idx}", "Last LinkedIn Message Submission Date", "Last LinkedIn Message Submission Date")
    action_button(col3, "✉️ Email", f"email_{idx}", "Last Email Submission Date", "Last Email Submission Date")
    action_button(col4, "📞 Call", f"call_{idx}", "Last Call Date", "Last Call Date")
    action_button(col5, "📅 Meeting", f"meeting_{idx}", "Last Meeting Date", "Last Meeting Date")
    # New "Add to cadence" button like LinkedIn button
    action_button(col6, "➕ Add to cadence", f"cadence_{idx}", "Last Add To Cadence Date", "Last Add To Cadence Date")

# Apply updates and rerun
if st.session_state.get("update_triggered", False):
    # Update main contacts_df
    for email, updates in st.session_state.contact_updates.items():
        idx_main = contacts_df.index[contacts_df["Email"] == email]
        if not idx_main.empty:
            idx_main = idx_main[0]
            for col, val in updates.items():
                contacts_df.at[idx_main, col] = val
            # Update account last contact date too
            if "Last Action Date" in updates and selected_rows and len(selected_rows) > 0:
                update_account_last_contact_date(accounts_df, selected_domain, pd.to_datetime(updates["Last Action Date"]))

    st.session_state.update_triggered = False
    try:
        st.experimental_rerun()
    except Exception:
        pass

if not selected_rows:
    st.info("Select an account from the table above to view contacts.")
