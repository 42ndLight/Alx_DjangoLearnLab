from django.shortcuts import render
from rest_framework.response import Response
from .models import Notifications
from .serializers import NotificationSerializer
from rest_framework import generics, permissions


# Create your views here.
class NotificationsListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notifications.objects.filter(recipient=self.request.user)

class NotificationsMarkAsReadView(generics.UpdateAPIView):
    queryset = Notifications.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializers):
        serializers.instance.mark_as_read()

class UnreadNotificationsCountView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        count  = Notifications.objects.filter(
            recipient=request.user,
            read=False
        ).count()
        return Response({'unread_count' : count})

    

