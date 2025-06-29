import os
import django
from decouple import config

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend_project.settings")
django.setup()

from telegram.ext import Updater, CommandHandler
from telegram_bot.models import TelegramUser

TELEGRAM_TOKEN = config('TELEGRAM_TOKEN')

def start(update, context):
    username = update.message.from_user.username
    chat_id = update.message.chat_id
    TelegramUser.objects.get_or_create(username=username, chat_id=chat_id)
    update.message.reply_text("Welcome! Your username has been saved.")

updater = Updater(TELEGRAM_TOKEN)
dp = updater.dispatcher
dp.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()
