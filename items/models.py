from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    NEW = 'new'
    USED = 'used'
    CONDITION_CHOICES = [
        (NEW, 'New'),
        (USED, 'Used'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='items/')
    condition = models.CharField(max_length=4, choices=CONDITION_CHOICES)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
