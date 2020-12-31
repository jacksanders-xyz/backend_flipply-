from django.db import models
from django.contrib.auth.models import User, AbstractUser


class User(AbstractUser):
    stance = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.username




