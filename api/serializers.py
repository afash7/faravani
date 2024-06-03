from rest_framework import serializers
from users.models import Profile
from items.models import Item
from communications.models import Chat, Message
from verification.models import VerificationCode
from uploads.models import Upload

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'photo', 'bio']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['title', 'description', 'category', 'image', 'condition', 'created_at', 'updated_at']

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['participants', 'created_at']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['chat', 'sender', 'content', 'timestamp']

class VerificationCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificationCode
        fields = ['user', 'code', 'created_at']

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = ['file', 'description']
