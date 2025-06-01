from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    def create(self, request, *args, **kwargs):
        participants_ids = request.data.get('participants', [])
        if not participants_ids:
            return Response({"error": "Participants are required to create a conversation."},
                            status=status.HTTP_400_BAD_REQUEST)
        
        conversation = Conversation.objects.create()
        conversation.participants.set(participants_ids)
        conversation.save()

        serializer = self.get_serializer(conversation)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def create(self, request, *args, **kwargs):
        conversation_id = request.data.get('conversation')
        sender_id = request.data.get('sender')
        content = request.data.get('message_body')

        if not all([conversation_id, sender_id, content]):
            return Response({"error": "Conversation, sender and message_body are required."},
                            status=status.HTTP_400_BAD_REQUEST)

        message = Message.objects.create(
            conversation_id=conversation_id,
            sender_id=sender_id,
            content=content
        )
        serializer = self.get_serializer(message)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
