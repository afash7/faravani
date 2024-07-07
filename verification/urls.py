from django.urls import path
from . import views

urlpatterns = [
    path('', views.verify_phone, name='verify_phone'),
    path('resend/', views.resend_verification_code, name='resend_verification_code'),
]
