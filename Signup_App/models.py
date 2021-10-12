from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver


# Create your models here.

class Registration(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=50, null=True)
    email = models.EmailField()
    password = models.CharField(max_length=12)
    confirm_password = models.CharField(max_length=12)

    def __str__(self):
        return self.first_name, self.last_name
