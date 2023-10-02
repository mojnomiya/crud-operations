from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=64)

    def __str__(self):
        return self.name