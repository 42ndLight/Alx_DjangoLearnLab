from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient')
    actor = models.ForeignKey(User,  on_delete=models.CASCADE, related_name='actot')
    verb = models.TextField()
    target_content_type = models.ForeignKey(ContentType, blank=True, null=True, on_delete=models.CASCADE)
    target_object_id = models.PositiveIntegerField(blank=True, null=True)
    target = GenericForeignKey('target_content_type', 'target_object_id')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.actor} {self.verb} {self.target or ''}"

    def mark_as_read(self):
        self.read = True
        self.save()
    
    def mark_as_unread(self):
        self.read = False
        self.save()
