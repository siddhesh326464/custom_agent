import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

from agent.agent import Agent
import tools.calculator
import tools.chat
import tools.filesystem
import tools.memory_tools

load_dotenv()

my_agent = Agent()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the /start command when you first message the bot"""
    await update.message.reply_text("Hello! I am your AI Agent. Send me a message and I will process it!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Receives your Telegram text and passes it to your Agent"""
    user_message = update.message.text
    print(f"\n[Telegram User]: {user_message}")
    
    try:
        answer = my_agent.run(query=user_message)
        
        print(f"[Agent Reply]: {answer}")
        
        await update.message.reply_text(answer)
        
    except Exception as e:
        error_msg = f"Oops, something went wrong: {e}"
        print(error_msg)
        await update.message.reply_text(error_msg)

if __name__ == '__main__':
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        print("ERROR: TELEGRAM_BOT_TOKEN not found in .env")
        exit(1)

    print("Starting Telegram Bot...")
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("Bot is online! Go to Telegram and send it a message.")
    app.run_polling()
