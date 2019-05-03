from django.db import models

# Create your models here.
class Photo(models.Model):
    image = models.ImageField(upload_to='uploaded_photos/')
    likes = models.IntegerField(default=0)
    taken_date = models.DateField(null=False)
    reviewed = models.BooleanField(default=False)