from django.db import models

# Create your models here.
class Profile(models.Model):
    name=models.CharField(max_length=70)
    comment=models.CharField(max_length=70)
    surname=models.CharField(max_length=40,default='Raj')
    def __str__(self):
        return str(self.id)

class User(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    def __str__(self):
        return str(self.name)