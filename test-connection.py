import streamlit as st
import json
from oauth2client.service_account import ServiceAccountCredentials
import gspread

st.title("Google Sheets Connection Test")

# -----------------------------
# AUTHENTICATE WITH STREAMLIT SECRET
# -----------------------------
try:
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/drive"]

    creds_dict = json.loads(st.secrets["google_creds"]["creds"])
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)

    st.success("✅ Authentication successful!")
    st.write("Service Account Email:", creds_dict["client_email"])

    # List all sheets the service account can see
    sheets = client.openall()
    st.write("Sheets visible to this service account:")
    for s in sheets:
        st.write("•", s.title)

except Exception as e:
    st.error("❌ Error connecting to Google Sheets")
    st.error(e)
