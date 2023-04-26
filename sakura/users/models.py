from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(
        'Почта',
        unique=True,
        max_length=50
    )
    city = models.CharField(
        'Город',
        max_length=50
    )
    address = models.CharField(
        'Адрес',
        max_length=100
    )


