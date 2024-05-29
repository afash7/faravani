from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('create/', views.item_create, name='item_create'),
    path('edit/<int:pk>/', views.item_update, name='item_update'),
    path('<int:pk>/', views.item_detail, name='item_detail'),
    path('delete/<int:pk>/', views.item_delete, name='item_delete'),
]
