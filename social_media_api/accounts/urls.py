from django.urls import path
from .views import RegisterUserView, LoginUserView, ProfileUserView, FollowUserView, UnfollowUserView
from rest_framework.authtoken import views

urlpatterns = {
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('profile/', ProfileUserView.as_view(), name='profile'),
    path('api-token-auth/', views.obtain_auth_token),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view, name='unfollow-user'),
}