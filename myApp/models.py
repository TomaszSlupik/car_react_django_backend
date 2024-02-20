from django.db import models

# Create your models here.
class Car (models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length= 20)

def __str__(self):
    return f"{self.id} {self.title}"