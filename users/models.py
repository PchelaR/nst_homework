from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Email")
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Телефон")
    bio = models.TextField(blank=True, null=True, verbose_name="О себе")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
