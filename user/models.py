from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    user = models.OneToOneField(User, related_name="user", on_delete=models.CASCADE)
    admin = models.BooleanField(default=True)
