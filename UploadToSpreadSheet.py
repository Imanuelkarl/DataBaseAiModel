import os
import sys
sys.path.append('/storage/emulated/0/Desktop/Python')  # Add the path to 'my_project' folder


from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']  # Required scope for Sheets API
credentials_path = r"C:\Users\DELL\Desktop\Python\credentials.json"   # Replace with your file path
SHEET_ID="1KEJD7kloAX-n7zn-D1x7Cew3VmxwtyloQbNkRri2mEQ"
SHEET_TITLE="subjectQuestions"

def get_service():
    credentials = Credentials.from_service_account_file(credentials_path, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=credentials)
    return service

def upload_data(data, spreadsheet_id, sheet_title):
    service = get_service()

    # Validate data format
    if not isinstance(data, list):
        raise ValueError("Data must be a list of lists (rows and columns)")

    body = {
        'values': data
    }

    # Assuming you want to write starting from cell A1
    range_name = f"{sheet_title}!A1:{chr(ord('A') + len(data[0]) - 1)}{len(data)}"

    try:
        service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=f"{sheet_title}!C689:G689",
            valueInputOption='USER_ENTERED',
            body=body
        ).execute()
        print("Data uploaded successfully!")
    except Exception as e:
        print(f"Error uploading data: {e}")


your_string = "Which spectroscopic technique is commonly used to study molecular vibrations in infrared spectroscopy?\nInelastic scattering spectroscopy\nRaman spectroscopy\nFourier transform infrared spectroscopy (FTIR)\nUltraviolet-visible spectroscopy"
data = [your_string.splitlines()]
upload_data(data,"1KEJD7kloAX-n7zn-D1x7Cew3VmxwtyloQbNkRri2mEQ","subjectQuestions")
