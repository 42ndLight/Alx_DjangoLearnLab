from django.urls import path
from .views import RegisterUserView, LoginUserView
from rest_framework.authtoken import views

urlpatterns = {
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('api-token-auth/', views.obtain_auth_token)
}