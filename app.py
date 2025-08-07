import streamlit as st
import pandas as pd
from datetime import datetime
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode

# 1. Sample Data
def load_sample_data():
    accounts = pd.DataFrame([
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
        }
    ])

    contacts = pd.DataFrame([
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
            "Last Meeting Date": ""
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
            "Last Meeting Date": ""
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
            "Last Meeting Date": "2025-07-30"
        }
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
if selected_rows:
    selected_account = selected_rows[0]
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

        with col2:
            if st.button("💬 LinkedIn Message", key=f"msg_{idx}"):
                contacts_df.at[row.name, "Last LinkedIn Message Submission Date"] = today
                contacts_df.at[row.name, "Last Action Date"] = today
                contacts_df.at[row.name, "Last Action Type Event"] = "LinkedIn Message"
                st.success("LinkedIn Message recorded.")

        with col3:
            if st.button("✉️ Email", key=f"email_{idx}"):
                contacts_df.at[row.name, "Last Email Submission Date"] = today
                contacts_df.at[row.name, "Last Action Date"] = today
                contacts_df.at[row.name, "Last Action Type Event"] = "Email"
                st.success("Email recorded.")

        with col4:
            if st.button("📞 Call", key=f"call_{idx}"):
                contacts_df.at[row.name, "Last Call Date"] = today
                contacts_df.at[row.name, "Last Action Date"] = today
                contacts_df.at[row.name, "Last Action Type Event"] = "Call"
                st.success("Call recorded.")

        with col5:
            if st.button("📅 Meeting", key=f"meeting_{idx}"):
                contacts_df.at[row.name, "Last Meeting Date"] = today
                contacts_df.at[row.name, "Last Action Date"] = today
                contacts_df.at[row.name, "Last Action Type Event"] = "Meeting"
                st.success("Meeting recorded.")
else:
    st.info("Select a row from the accounts table above to view and act on contacts.")
