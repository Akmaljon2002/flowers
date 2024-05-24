from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = "Users"
