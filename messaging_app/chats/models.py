from django.db import models
from django.contrib.auth.models import AbstractUser


# Custom user model extending Django's built-in AbstractUser
# This allows adding extra fields later if needed while keeping all default auth features
class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    last_seen = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.username


# Model representing a conversation between multiple users (many-to-many relationship)
class Conversation(models.Model):
    participants = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the conversation was created

    def __str__(self):
        return f"Conversation {self.id} with {self.participants.count()} participants"


# Model representing a single message in a conversation
class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    content = models.TextField()  # Message body
    timestamp = models.DateTimeField(auto_now_add=True)  # Time when the message was sent

    def __str__(self):
        return f"Message {self.id} from {self.sender.username} in Conversation {self.conversation.id}"
