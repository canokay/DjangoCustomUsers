from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Username")
    userStatus = models.ForeignKey(
        'CustomUsers.UserStatus', on_delete=models.CASCADE, verbose_name='User Status')

    def __str__(self):
        return f'{self.user.username} Profile'

    class Meta:
        verbose_name = 'User Detail'
        verbose_name_plural = 'User Details'


class UserStatus(models.Model):
    userStatus = models.CharField(max_length=40, verbose_name="User Status")

    class Meta:
        verbose_name = 'User Status'
        verbose_name_plural = 'User Statuses'

    def __str__(self):
        return self.userStatus
