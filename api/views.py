from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import TelegramUser
from django.contrib.auth.models import User
from .tasks import send_welcome_email
from rest_framework.views import APIView

@api_view(['GET'])
@permission_classes([AllowAny])
def public_view(request):
    return Response({"message": "This is a public endpoint"})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({"message": f"Hello, {request.user.username}"})

@api_view(['POST'])
def telegram_webhook(request):
    data = request.data
    
    TelegramUser.objects.update_or_create(
        telegram_id=data.get('telegram_id'),
        defaults={
            'username': data.get('username'),
            'first_name': data.get('first_name'),
            'last_name': data.get('last_name'),
        }
        
    )
    return Response({"message": "User saved successfully"})

class RegisterUserView(APIView):
    def post(self, request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        user = User.objects.create_user(username=username, email=email, password=password)

        # ✅ Now send email after user is created
        send_welcome_email.delay(user.email)

        return Response({"message": "User registered and email sent!"})

# Create your views here.
