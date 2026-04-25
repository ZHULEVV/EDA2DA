from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, ProfileView

urlpatterns = [
    # Вход (получение токена)
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Обновление токена
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Регистрация
    path('register/', RegisterView.as_view(), name='auth_register'),
    # Информация о текущем пользователе
    path('me/', ProfileView.as_view(), name='user_profile'),
]