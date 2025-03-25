from django.urls import path
from .views import RegisterUserView, LoginUserView, ProfileUserView
from rest_framework.authtoken import views

urlpatterns = {
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('profile/', ProfileUserView.as_view(), name='profile'),
    path('api-token-auth/', views.obtain_auth_token)
}