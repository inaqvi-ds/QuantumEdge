import streamlit as st
import pandas as pd
from datetime import datetime

# Sample job data
data = [
    {"Company": "Google", "Role": "Data Scientist", "Location": "Mountain View, CA", "Status": "Applied", "Posted": "2025-10-20"},
    {"Company": "Waymo", "Role": "DevOps Engineer", "Location": "Mountain View, CA", "Status": "Saved", "Posted": "2025-10-22"},
    {"Company": "LinkedIn", "Role": "Project Manager", "Location": "Sunnyvale, CA", "Status": "Interviewing", "Posted": "2025-10-18"},
]

df = pd.DataFrame(data)

# Sidebar filters
st.sidebar.header("🔍 Filter Jobs")
role_filter = st.sidebar.multiselect("Role Type", options=df["Role"].unique(), default=df["Role"].unique())
status_filter = st.sidebar.multiselect("Application Status", options=df["Status"].unique(), default=df["Status"].unique())

# Filtered data
filtered_df = df[df["Role"].isin(role_filter) & df["Status"].isin(status_filter)]

# Dashboard
st.title("📊 Job Application Tracker")
st.write(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

st.dataframe(filtered_df)

# Summary charts
st.subheader("📌 Applications by Status")
st.bar_chart(df["Status"].value_counts())

st.subheader("🏢 Roles by Company")
st.bar_chart(df["Company"].value_counts())

# Add new job entry
st.subheader("➕ Add New Job")
with st.form("new_job_form"):
    company = st.text_input("Company")
    role = st.selectbox("Role", ["Data Scientist", "Project Manager", "DevOps Engineer", "System Engineer"])
    location = st.text_input("Location")
    status = st.selectbox("Status", ["Saved", "Applied", "Interviewing", "Rejected"])
    posted = st.date_input("Date Posted", value=datetime.today())
    submitted = st.form_submit_button("Add Job")

    if submitted:
        new_entry = {
            "Company": company,
            "Role": role,
            "Location": location,
            "Status": status,
            "Posted": posted.strftime("%Y-%m-%d")
        }
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        st.success(f"Added job at {company}!")
