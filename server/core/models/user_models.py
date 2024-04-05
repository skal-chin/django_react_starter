from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from core.managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):

    class Meta:
        db_table = 'core_customuser'

    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email