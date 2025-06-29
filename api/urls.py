from django.urls import path
from .views import public_view, protected_view
from .views import telegram_webhook,RegisterUserView

urlpatterns = [
    path('public/', public_view),
    path('protected/', protected_view),
    path('telegram/', telegram_webhook),
    path('register/', RegisterUserView.as_view()),
]
