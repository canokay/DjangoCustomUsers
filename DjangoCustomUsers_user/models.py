from django.db import models
from django.db.models import ImageField, CharField, DateField, TextField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDERS = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    USER_STATUS = (
        ('admin','Admin'),
        ('editor','Editor'),
    )
    user_status = CharField(max_length=20, null=True, blank=True, verbose_name='User Status', choices=USER_STATUS)
    profile_photo = ImageField(verbose_name='Profile Photo', upload_to='images/user/profile/', blank=True, null=True)
    gender = CharField(max_length=10, null=True, blank=True, verbose_name='Gender', choices=GENDERS)
    birthday = DateField(null=True, blank=True, verbose_name='Birthday')
    bio = TextField(blank=True, null=True, verbose_name='Biography')
    phone = CharField(max_length=100, null=True, blank=True, verbose_name='Phone')

    class Meta:
        verbose_name = 'Kullanıcı'
        verbose_name_plural = 'Tüm Kullanıcılar'
