from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import UserRegisterSerializer, UserSerializer
from .models import User

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,) # Регистрация доступна всем
    serializer_class = UserRegisterSerializer

class ProfileView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,) # Только для вошедших пользователей
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user