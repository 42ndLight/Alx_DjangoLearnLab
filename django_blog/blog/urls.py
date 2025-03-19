from django.urls import path
from .views import profile_view, register, login, logout

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('profile/', profile_view, name='profile'),
]