from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
    subject = models.CharField(max_length=100, blank=True, null=True)
    body = models.TextField()
    timestamp = models.DateTimeField(default=now)
    is_read = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)  # Control de mensajes activos/inactivos

    def __str__(self):
        return f"From {self.sender} to {self.recipient} at {self.timestamp}"




