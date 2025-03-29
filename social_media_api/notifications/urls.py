from django.urls import path
from .views import (
    NotificationsListView,
    NotificationsMarkAsReadView,
    UnreadNotificationsCountView
)

urlpatterns = [
    path('', NotificationsListView.as_view(), name='notification-list'),
    path('<int:pk>/read/', NotificationsMarkAsReadView.as_view(), name='notification-read'),
    path('unread-count/', UnreadNotificationsCountView.as_view(), name='unread-count'),
]