from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    def __str__(self):
        return self.username
