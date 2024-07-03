from django.contrib import admin
from .models import Upload

class UploadAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'uploaded_at', 'description')
    search_fields = ('user__username', 'description')
    list_filter = ('uploaded_at',)

admin.site.register(Upload, UploadAdmin)
