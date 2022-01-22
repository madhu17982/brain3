from django.db import models

# Create your models here.

class Item(models.Model):
    word= models.CharField(max_length=1000)
    answer=models.TextField()
