from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    status = models.CharField(max_length=30, null=True,
                              blank=True, verbose_name='Kullanıcı Durumu')

    class Meta:
        verbose_name = 'Kullanıcı'
        verbose_name_plural = 'Tüm Kullanıcılar'
