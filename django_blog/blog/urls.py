from django.urls import path
from .views import profile_view, register, user_login, user_logout, ListPostView, DetailPostView, CreatePostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('posts', ListPostView.as_view(), name='index'),
    path('post/<int:pk>', DetailPostView.as_view(), name='detail'),
    path('post/new/', CreatePostView.as_view(), name='create'),
    path('post/<int:pk>/edit/', UpdatePostView.as_view(), name='edit'),
    path('post/<int:pk>/delete/', DeletePostView.as_view(), name='delete'),
]