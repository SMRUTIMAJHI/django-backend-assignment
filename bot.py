import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

user_states = {}

API_URL = "http://localhost:8000/api/register/"
DJANGO_ENDPOINT = "http://localhost:8000/api/telegram/"
TOKEN = '7108508232:AAGbxbW8nkjOyBGXjcUC28S8d5v_KRmydcY'

def start(update, context):
    update.message.reply_text("👋 Welcome! Please enter your desired username.")
    user_states[update.message.chat_id] = {"step": "username"}

def handle_message(update, context):
    user_id = update.message.chat_id
    text = update.message.text

    # Get current step or default to asking username
    state = user_states.get(user_id, {}).get("step", "username")

    if state == "username":
        user_states[user_id] = {"step": "email", "username": text}
        update.message.reply_text("📧 Please enter your email.")

    elif state == "email":
        user_states[user_id]["email"] = text
        user_states[user_id]["step"] = "password"
        update.message.reply_text("🔐 Please enter your password.")

    elif state == "password":
        user_data = user_states[user_id]
        user_data["password"] = text

        # Send registration data to Django backend
        try:
            response = requests.post(API_URL, json={
                "username": user_data["username"],
                "email": user_data["email"],
                "password": user_data["password"]
            })

            if response.status_code in [200, 201]:
                update.message.reply_text("✅ You are registered! A welcome email has been sent.")

                # Now save Telegram user info
                user = update.message.from_user
                telegram_payload = {
                    "telegram_id": user.id,
                    "username": user.username,
                    "first_name": user.first_name,
                    "last_name": user.last_name
                }

                telegram_response = requests.post(DJANGO_ENDPOINT, json=telegram_payload)

                if telegram_response.status_code == 200:
                    update.message.reply_text("🗃️ Your Telegram info has been saved.")
                else:
                    update.message.reply_text("⚠️ Failed to save Telegram info.")

            else:
                update.message.reply_text("⚠️ Registration failed. Please try again.")

        except Exception as e:
            update.message.reply_text(f"❌ Error: {str(e)}")

        # Clear user state
        user_states.pop(user_id, None)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
