import google.generativeai as genai 

API_KEY='AIzaSyBagutCVmzinNYXn_JiQYumvSbE7QB-27c'


genai.configure(
    api_key=API_KEY
)

model =genai.GenerativeModel('gemini-pro')
chat=model.start_chat(history=[])

while(True):
    question =input("You: ")
    response = chat.send_message(question)
    print('\n')
    print(f"Bot: {response.text}")
    print('\n')
    
def getPrompt(text_input):
    question=text_input
    response = chat.send_message(question)
    print('\n')
    
    return print(f"Bot: {response.text}")
    