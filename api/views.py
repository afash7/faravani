from rest_framework import viewsets
from users.models import Profile
from items.models import Item
from communications.models import Chat, Message
from verification.models import VerificationCode
from uploads.models import Upload
from .serializers import ProfileSerializer, ItemSerializer, ChatSerializer, MessageSerializer, VerificationCodeSerializer, UploadSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class VerificationCodeViewSet(viewsets.ModelViewSet):
    queryset = VerificationCode.objects.all()
    serializer_class = VerificationCodeSerializer

class UploadViewSet(viewsets.ModelViewSet):
    queryset = Upload.objects.all()
    serializer_class = UploadSerializer
