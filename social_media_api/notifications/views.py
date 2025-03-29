from django.shortcuts import render
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework import generics, permissions


# Create your views here.
class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user)

class NotificationMarkAsReadView(generics.UpdateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializers):
        serializers.instance.mark_as_read()

class UnreadNotificationCountView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        count  = Notification.objects.filter(
            recipient=request.user,
            read=False
        ).count()
        return Response({'unread_count' : count})

    

