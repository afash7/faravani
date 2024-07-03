from django.contrib import admin
from .models import Category, Item, Request

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'condition', 'owner', 'created_at')
    search_fields = ('title', 'description', 'category__name', 'owner__username')
    list_filter = ('category', 'condition', 'owner', 'created_at')

class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'requester', 'status', 'created_at')
    search_fields = ('item__title', 'requester__username', 'message')
    list_filter = ('status', 'created_at')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Request, RequestAdmin)
