from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    avatar = models.CharField(max_length=20, verbose_name="تصویر اواتار", null=True, blank=True)
    email_active_code = models.CharField(max_length=20, verbose_name="تلفن همراه")
    about_user = models.TextField(verbose_name='درباره شخص',null=True,blank=True)

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.first_name is not '' and self.last_name is not '':
            return self.get_full_name()
        return self.email
