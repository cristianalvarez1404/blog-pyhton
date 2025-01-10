from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Write(models.Model):
    title = models.TextField(max_length=255)
    description = models.TextField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)