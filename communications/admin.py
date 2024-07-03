from django.contrib import admin
from .models import Chat, Message

class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'participants_display')
    search_fields = ('participants__username',)

    def participants_display(self, obj):
        return ', '.join(participant.username for participant in obj.participants.all())
    participants_display.short_description = 'Participants'

class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'chat', 'sender', 'recipient', 'timestamp', 'content')
    search_fields = ('sender__username', 'recipient__username', 'content')
    list_filter = ('chat', 'sender', 'recipient', 'timestamp')

admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)
