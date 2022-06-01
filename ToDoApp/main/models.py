from django.db import models

# Create your models here.
class ToDO(models.Model):
    date = models.DateTimeField()
    text = models.CharField(max_length=200)

    