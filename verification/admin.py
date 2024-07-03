from django.contrib import admin
from .models import VerificationCode

class VerificationCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'code', 'created_at', 'is_verified')
    search_fields = ('user__username', 'code')
    list_filter = ('created_at', 'is_verified')

admin.site.register(VerificationCode, VerificationCodeAdmin)
