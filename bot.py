import os
from telegram.ext import Updater, CommandHandler

BOT_TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    update.message.reply_text("Bot chal raha hai ✔️")

def menu(update, context):
    update.message.reply_text("Ye raha aapka menu button")

updater = Updater(BOT_TOKEN)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("menu", menu))

updater.start_polling()
