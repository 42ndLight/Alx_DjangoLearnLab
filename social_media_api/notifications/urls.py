from django.urls import path
from .views import (
    NotificationListView,
    NotificationMarkAsReadView,
    UnreadNotificationCountView
)

urlpatterns = [
    path('', NotificationListView.as_view(), name='notification-list'),
    path('<int:pk>/read/', NotificationMarkAsReadView.as_view(), name='notification-read'),
    path('unread-count/', UnreadNotificationCountView.as_view(), name='unread-count'),
]