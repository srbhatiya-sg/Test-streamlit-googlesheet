import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import json

st.title("Google Sheets Connection Test (Updated)")

try:
    # Load credentials from Streamlit Secrets
    creds_dict = json.loads(st.secrets["google_creds"]["creds"])

    # Define scopes
    scopes = ["https://www.googleapis.com/auth/spreadsheets",
              "https://www.googleapis.com/auth/drive"]

    # Create Credentials object
    creds = Credentials.from_service_account_info(creds_dict, scopes=scopes)

    # Authorize gspread client
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
