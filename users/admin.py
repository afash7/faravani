from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'phone_number', 'address', 'date_of_birth')
    search_fields = ('user__username', 'phone_number', 'address')
    list_filter = ('date_of_birth',)

admin.site.register(Profile, ProfileAdmin)
