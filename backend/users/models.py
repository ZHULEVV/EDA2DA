from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    role = models.CharField(max_length=20, default='USER')
    is_subscriber = models.BooleanField(default=False)
    preferences = models.JSONField(default=list, blank=True)