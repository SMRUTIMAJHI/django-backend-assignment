from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_welcome_email(email):
    send_mail(
        subject='Welcome!',
        message='Thank you for registering!',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
        
    )
    print(f"Sending welcome email to {email}")
