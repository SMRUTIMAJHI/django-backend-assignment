# Django Backend Assignment 🚀

A backend project built with **Django**, **Django REST Framework**, **JWT Authentication**, **Celery with Redis**, and **Telegram Bot integration**.

---

## 📁 Project Structure

django-backend-assignment/
├── api/                    # Django app with models, views, serializers, tasks
├── backend_project/        # Project settings and Celery configuration
├── telegram_bot/           # Only for models, migrations, and any related business logic
├── bot.py                  # Telegram bot main entrypoint
├── test_redis.py           # Redis test script
├── db.sqlite3              # SQLite database file (auto-generated)
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not committed to Git)
├── .gitignore              # Git ignore rules
├── env/                    # Python virtual environment (excluded from Git)
└── README.md               # Project documentation


---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/SMRUTIMAJHI/django-backend-assignment.git
   cd django-backend-assignment
2. Create a virtual environment
python -m venv env
env\Scripts\activate  # On Windows

3.Install dependencies
pip install -r requirements.txt

4.Create .env file
SECRET_KEY=your_django_secret_key
DEBUG=True

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
EMAIL_USE_TLS=True

TELEGRAM_TOKEN=your_telegram_bot_token
5. Apply migrations
python manage.py migrate

6. Run the Django server
python manage.py runserver

7.Start Celery worker
celery -A backend_project worker --loglevel=info --pool=solo

🤖 Telegram Bot- My bot name is SmrutiBot
Interacts via /start command

Collects user info: username, email, password

Registers to backend via REST API

Sends confirmation email using Celery

Code: bot.py

🔐 Authentication
/api/register/ – Registers a new user

/api/public/ – Open access

/api/protected/ – JWT token required

📬 Email Sending
After user registration (via Telegram), a welcome email is sent asynchronously using Celery and Gmail SMTP.

🔗 API Endpoints
Method	URL	Description
POST	/api/register/	User registration
POST	/api/telegram/	Telegram user registration
GET	/api/public/	Open test view
GET	/api/protected/	JWT protected view

❗ Environment Variables
Ensure the following variables are set in .env:

SECRET_KEY=your_django_secret_key
DEBUG=True

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
EMAIL_USE_TLS=True

TELEGRAM_TOKEN=your_telegram_bot_token
✅ Use Gmail App Passwords if 2FA is enabled.

👩‍💻 Author
Made with ❤️ by Smruti Majhi
---
Let me know if you'd like to include screenshots or live demo links.
