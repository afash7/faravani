"""
Developer: afash.ir
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path("blog/", include("blog.urls")),
    path('users/', include('users.urls')),
    path('items/', include('items.urls')),
    path('communications/', include('communications.urls')),
    path('verification/', include('verification.urls')),
    path('uploads/', include('uploads.urls')),
    path('api/', include('api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
