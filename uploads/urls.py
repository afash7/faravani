from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_list, name='upload_list'),
    path('upload/', views.upload_image, name='upload_image'),
]
