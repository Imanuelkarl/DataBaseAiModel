import sys
sys.path.append(r'C:\Users\DELL\Desktop\Python')  # Add the path to 'my_project' folder

import PythonDatabaseManager
from typing import Final
from telegram import Update
from telegram.ext import Application,CommandHandler, MessageHandler, filters, ContextTypes

TOKEN : Final = "hidden"
Bot_Username :Final="@taptapdatabasebot"



async def start_Command(update: Update,context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello and welcome to my AI")
    
    
async def help_Command(update: Update,context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello and welcome to my AI")
    
    
async def hello_Command(update: Update,context : ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello and welcome to my AI")
    
    
    
def handle_response(text : str):
    
    processed : str = text.lower()
    
    if "hello" in processed:
        return "Hi what can i do for you today"
        
    if "how are you" in processed:
        return "I'm good and you"
    else:
        PythonDatabaseManager.convert_text_to_question(text)
        return PythonDatabaseManager.display()
        
    return "i do not understand you please"
    
    
async def handle_image(update :Update, context :ContextTypes.DEFAULT_TYPE):
    photo = update.message.photo[-1]  # Get the largest available photo
    file_id = photo.file_id
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=photo.file_id)
    
async def handle_message(update : Update, context : ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}" ')
    if message_type == "group":
        if Bot_Username in text:
            new_text:str =text.replace(Bot_Username," ").strip()
            response: str = handle_response(new_text)
        else :
            return
    else:
        response: str = handle_response(text)
        
        
    print("Bot:",response)
    await update.message.reply_text(response)
    
    
    
async def error(update: Update,context : ContextTypes.DEFAULT_TYPE):
    print(f' Update {update} caused error {context.error}')
    
    
    
if __name__ == "__main__":
    app= Application.builder().token(TOKEN).build()
    print("Starting...")
    app.add_handler(CommandHandler("start",start_Command))
    app.add_handler(CommandHandler("help",help_Command))
    app.add_handler(CommandHandler("hello",hello_Command))
    app.add_handler(MessageHandler(filters.TEXT,handle_message))
    app.add_handler(MessageHandler(filters.PHOTO, handle_image))
    app.add_error_handler(error)
    
    print("Polling...")
    app.run_polling(poll_interval=3)
    
