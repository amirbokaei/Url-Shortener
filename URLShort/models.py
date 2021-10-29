from django.db import models

# Create your models here.

class url_shorten(models.Model):
    orgin_url = models.CharField(max_length=300 , unique=True)
    short_url = models.CharField(max_length=100 , unique=True)