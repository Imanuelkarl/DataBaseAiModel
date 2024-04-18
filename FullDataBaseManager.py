import sys
import os
import google.generativeai as genai 


from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

API_KEY='AIzaSyBagutCVmzinNYXn_JiQYumvSbE7QB-27c'

genai.configure(
    api_key=API_KEY
)

model =genai.GenerativeModel('gemini-pro')
chat=model.start_chat(history=[])

sys.path.append(r'C:\Users\DELL\Desktop\Python')
questions=[]
answers=[]
wrongAnswers=[]
numbers=[]
lines=[]
options=[]

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
def convert_text_to_question(text_input_original):
    
    text_input=text_input_original.replace("\n"," ")
    number=text_input.split("**Question 2:**",1)[0]
    remaining=text_input.split("**Question 2:**",1)[1]
    numbers.append(number)
    number=remaining.split("**Question 3:**",1)[0]
    remaining=remaining.split("**Question 3:**",1)[1]
    numbers.append(number)
    numbers.append(remaining)
    for i in range(len(numbers)):
        question=numbers[i].split("(a)",1)[0]
        if "**Question 1:**" in question:
            question=question.replace("**Question 1:**"," ").strip()
        questions.append(question)
        remain=numbers[i].split("(a) ",1)[1]
        option=remain.split("(b) ",1)[0].strip()
        options.append(option)
        remain=remain.split("(b) ",1)[1]
        option=remain.split("(c) ",1)[0].strip()
        options.append(option)
        remain=remain.split("(c) ",1)[1]
        option=remain.split("(d) ",1)[0].strip()
        options.append(option)
        remain=remain.split("(d) ",1)[1].strip()
        option=remain.split("**Correct Answer:**",1)[0].strip()
        options.append(option)
        remain=remain.split("**Correct Answer:**",1)[1].strip()
        answers.append(remain)
     
    for i in range(len(answers)):
        if "(a)" in answers[i]:
            answers[i]=answers[i].replace("(a) ","")
        elif "(b)" in answers[i]:
            answers[i]=answers[i].replace("(b) ","")
        elif "(c)" in answers[i]:
            answers[i]=answers[i].replace("(c) ","")
        elif "(d)" in answers[i]:
            answers[i]=answers[i].replace("(d) ","")
        
    for i in range(0,len(options)):
        
       if not(options[i] == answers[0] or options[i] == answers[1] or options[i] == answers[2]):
           wrongAnswers.append(options[i])
            
               
    
    for p in range(len(answers)):
        print(answers[p])
    
    return len(wrongAnswers)

def upload_data(data, startAt,stopAt):
    service = get_service()

    # Validate data format
    if not isinstance(data, list):
        raise ValueError("Data must be a list of lists (rows and columns)")

    body = {
        'values': data
    }
    sheet_title2="subjectQuestions"
    # Assuming you want to write starting from cell A1
    range_name = f"{sheet_title2}!A1:{chr(ord('A') + len(data[0]) - 1)}{len(data)}"

    try:
        service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=f"{sheet_title2}!C{startAt}:G{stopAt}",
            valueInputOption='USER_ENTERED',
            body=body
        ).execute()
        print("Data uploaded successfully!")
    except Exception as e:
        print(f"Error uploading data: {e}")


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
    
    
subjects=getValues(234,251)

for i in range(len(subjects)):
    prompt="For this course "+subjects[i]+ " create 3 questions that has 4 options each where only one option is correct indicate the correct answer let it be the first option sample '**Question 1:**\n\nWhich of the following is NOT a property of a thermodynamic system?\n\n(a) Temperature\n(b) Volume\n(c) Position\n(d) Pressure\n\n**Correct Answer:** (c) Position\n\n**Question 2:**\n\nAn isolated system is one that:\n\n(a) Exchanges no mass or energy with its surroundings\n(b) Exchanges mass but not energy with its surroundings\n(c) Exchanges energy but not mass with its surroundings\n(d) Is in equilibrium and has no net change\n\n**Correct Answer:** (a) Exchanges no mass or energy with its surroundings\n\n**Question 3:**\n\nThe first law of thermodynamics states that:\n\n(a) Energy cannot be created or destroyed, only changed in form\n(b) Entropy of an isolated system always increases\n(c) Temperature of a system will always decrease over time(d) Pressure and volume of a gas are inversely proportional\n\n**Correct Answer:** (a) Energy cannot be created or destroyed, only changed in form'"
    response = chat.send_message(prompt)
    print(response.text)
    numbers=[]
    questions=[]
    answers=[]
    options=[]
    wrongAnswers=[]
    convert_text_to_question(response.text)
    for j in range(len(questions)):
        newText=questions[j]+"\n"+answers[j]+"\n"+wrongAnswers[j*3]+"\n"+wrongAnswers[j*3+1]+"\n"+wrongAnswers[j*3+2]
        data = [newText.splitlines()]
        upload_data(data,697+j+3*i,697+j+3*i)
