from rest_framework import serializers
from .models import Notifications

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField()
    target = serializers.StringRelatedField()

    class Meta:
        model = Notifications
        fields = ['id', 'actor', 'verb', 'target', 'timestamp', 'read']


    def get_target(self, obj):
        if obj.target:
            return str(obj.target)


        