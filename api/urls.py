from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)
router.register(r'items', views.ItemViewSet)
router.register(r'chats', views.ChatViewSet)
router.register(r'messages', views.MessageViewSet)
router.register(r'verification-codes', views.VerificationCodeViewSet)
router.register(r'uploads', views.UploadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
