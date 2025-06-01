from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from rest_framework import filters


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['participants__username', 'participants__email']  # Search by participant username/email
    
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
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['sender__username', 'content']
    ordering_fields = ['timestamp']
    ordering = ['-timestamp']

    def create(self, request, *args, **kwargs):
        conversation_id = request.data.get('conversation')
        sender_id = request.data.get('sender')
        content = request.data.get('content')  # Changed here to match model field

        if not all([conversation_id, sender_id, content]):
            return Response({"error": "Conversation, sender and content are required."},
                            status=status.HTTP_400_BAD_REQUEST)

        message = Message.objects.create(
            conversation_id=conversation_id,
            sender_id=sender_id,
            content=content
        )
        serializer = self.get_serializer(message)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
