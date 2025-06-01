from rest_framework import serializers
from .models import User, Conversation, Message


# Serializer for the User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "user_id", "username", "first_name", "last_name", "email",
            "bio", "phone_number", "profile_picture", "last_seen"
        ]


# Serializer for the Message model
class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)  # Nested user info

    class Meta:
        model = Message
        fields = [
            "message_id", "sender", "message_body", "sent_at", "conversation"
        ]


# Serializer for the Conversation model, includes nested messages
class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = [
            "conversation_id", "participants", "created_at", "messages"
        ]
