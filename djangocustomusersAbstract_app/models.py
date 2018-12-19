from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    status = models.CharField(max_length=30, null=True,
                              blank=True, verbose_name='User Status')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'All Users'
