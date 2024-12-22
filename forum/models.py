from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Topic(models.Model):
    title = models.CharField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="topics")
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.title

class Reply(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="replies")
    content = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="replies")
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"Reply by {self.creator} on {self.topic}"
