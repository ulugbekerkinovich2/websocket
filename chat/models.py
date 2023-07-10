from django.db import models
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Conversation(models.Model):
    initiator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="convo_starter"
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="convo_participant"
    )
    start_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.initiator} to {self.receiver}"


class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                               null=True, related_name='message_sender')
    text = models.CharField(max_length=200, blank=True)
    attachment = models.FileField(blank=True)
    conversation_id = models.ForeignKey(Conversation, on_delete=models.CASCADE, )
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return f"{self.sender} to {self.conversation_id}"


class Conversation_NEW(models.Model):
    room_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'Room: {self.room_name} ID:{str(self.id)}'


class Message_NEW(models.Model):
    conversation = models.ForeignKey(Conversation_NEW, on_delete=models.CASCADE)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
