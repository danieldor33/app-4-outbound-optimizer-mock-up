import streamlit as st
import pandas as pd
from datetime import datetime
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode

# 1. Sample Data
def load_sample_data():
    accounts = pd.DataFrame([
        # Original accounts
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
        # Additional accounts
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


# 2. Page Setup
st.set_page_config(layout="wide")
st.title("🧭 Seller Prioritization Assistant")

# 3. Load Data
accounts_df, contacts_df = load_sample_data()

# 4. Display Account Table (AgGrid)
st.subheader("Accounts Overview")

gb = GridOptionsBuilder.from_dataframe(accounts_df)
gb.configure_selection("single", use_checkbox=True)
grid_options = gb.build()

grid_response = AgGrid(
    accounts_df,
    gridOptions=grid_options,
    update_mode=GridUpdateMode.SELECTION_CHANGED,
    theme="streamlit",
    height=300,
    fit_columns_on_grid_load=True,
)

selected_rows = grid_response["selected_rows"]

# 5. Display Contacts if an Account is Selected
if not selected_rows.empty:
    selected_account = selected_rows.iloc[0]
    selected_domain = selected_account["Parent Company Domain"]

    st.subheader(f"Contacts for {selected_account['Account Name']}")

    filtered_contacts_df = contacts_df[contacts_df["Domain"] == selected_domain].reset_index(drop=True)

  for idx, row in filtered_contacts_df.iterrows():
    st.markdown(f"### {row['First Name']} {row['Last Name']}")
    st.write(f"📍 {row['Country']} | ✉️ {row['Email']} | 📞 {row['Phone']}")
    st.write(f"🕒 Last Action: {row['Last Action Type Event']} on {row['Last Action Date']}")

    col1, col2, col3, col4, col5 = st.columns(5)
    today = datetime.today().date()

    with col1:
        if st.button("📇 LinkedIn Connect", key=f"connect_{idx}"):
            contacts_df.at[row.name, "Last LinkedIn Connect Submission Date"] = today
            contacts_df.at[row.name, "Last Action Date"] = today
            contacts_df.at[row.name, "Last Action Type Event"] = "LinkedIn Connect submission"
            st.success("LinkedIn Connect recorded.")
        # Show last LinkedIn Connect date below button
        last_date = contacts_df.at[row.name, "Last LinkedIn Connect Submission Date"]
        st.caption(f"Last: {last_date if last_date else 'Never'}")

    with col2:
        if st.button("💬 LinkedIn Message", key=f"msg_{idx}"):
            contacts_df.at[row.name, "Last LinkedIn Message Submission Date"] = today
            contacts_df.at[row.name, "Last Action Date"] = today
            contacts_df.at[row.name, "Last Action Type Event"] = "LinkedIn Message"
            st.success("LinkedIn Message recorded.")
        last_date = contacts_df.at[row.name, "Last LinkedIn Message Submission Date"]
        st.caption(f"Last: {last_date if last_date else 'Never'}")

    with col3:
        if st.button("✉️ Email", key=f"email_{idx}"):
            contacts_df.at[row.name, "Last Email Submission Date"] = today
            contacts_df.at[row.name, "Last Action Date"] = today
            contacts_df.at[row.name, "Last Action Type Event"] = "Email"
            st.success("Email recorded.")
        last_date = contacts_df.at[row.name, "Last Email Submission Date"]
        st.caption(f"Last: {last_date if last_date else 'Never'}")

    with col4:
        if st.button("📞 Call", key=f"call_{idx}"):
            contacts_df.at[row.name, "Last Call Date"] = today
            contacts_df.at[row.name, "Last Action Date"] = today
            contacts_df.at[row.name, "Last Action Type Event"] = "Call"
            st.success("Call recorded.")
        last_date = contacts_df.at[row.name, "Last Call Date"]
        st.caption(f"Last: {last_date if last_date else 'Never'}")

    with col5:
        if st.button("📅 Meeting", key=f"meeting_{idx}"):
            contacts_df.at[row.name, "Last Meeting Date"] = today
            contacts_df.at[row.name, "Last Action Date"] = today
            contacts_df.at[row.name, "Last Action Type Event"] = "Meeting"
            st.success("Meeting recorded.")
        last_date = contacts_df.at[row.name, "Last Meeting Date"]
        st.caption(f"Last: {last_date if last_date else 'Never'}")
else:
    st.info("Select a row from the accounts table above to view and act on contacts.")
