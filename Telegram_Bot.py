# Telegram_Bot.py
from cryptography.fernet import Fernet
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


# 8/14/2025
# Telegram Bot To Generate Key Anonymously
# AUX-441

BOT_TOKEN = "8259404058:AAGx0cajNmo2uCUpqtcJW1iMQuuI8qZZWk0" # ( example 8259404058:AAGx0cajNmo2u ) # this will not work
        # you will need to Create your Bot in Botfather and Paste the Robot Token here .


user_chat_id = None
_last_key = None


class GetKeyBot:

    @staticmethod
    async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
        global user_chat_id
        user_chat_id = update.effective_chat.id
        await update.message.reply_text("Hello! Chat ID Saved Success.")

    @staticmethod
    async def getkey(update: Update, context: ContextTypes.DEFAULT_TYPE):
        global _last_key
        _last_key = Fernet.generate_key()
        await update.message.reply_text(_last_key.decode())
        return _last_key


def get_last_key():
    global _last_key
    return _last_key


def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", GetKeyBot.start))
    app.add_handler(CommandHandler("getkey", GetKeyBot.getkey))

    print("Bot Started Successfully. Waiting for ( /start , /getkey ) commands.")
    app.run_polling()
