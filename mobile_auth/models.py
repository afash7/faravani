from django.db import models

class UserMobileAuth(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)