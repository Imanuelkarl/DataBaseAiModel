from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

# Replace these with your actual credentials
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']  # Read-only access for sheets
credentials = None
credentials_path = r"C:\Users\DELL\Desktop\Python\credentials.json" 

def get_service():
    credentials = Credentials.from_service_account_file(credentials_path, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=credentials)
    return service

service=get_service()
# Spreadsheet ID and sheet name
spreadsheet_id = '1KEJD7kloAX-n7zn-D1x7Cew3VmxwtyloQbNkRri2mEQ'
sheet_name = 'courseSubjects'  # Adjust if your data is in a different sheet

# Option 2: Get data from a specific range
def getValues(startAt,stopAt):
    start_row = startAt  # Adjust this to the starting row (inclusive)
    end_row = stopAt  # Adjust this to the ending row (inclusive)
    range_string = f'{sheet_name}!C{start_row}:C{end_row}'
    # Make the API request
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_string).execute()
    # Handle empty response
    if 'values' not in result:
        print('No data found in the specified range.')
    else:
        range_values = [str(cell) for row in result['values'] for cell in row]
        print(range_values)
        return range_values
    
    
getValues(232,249)
