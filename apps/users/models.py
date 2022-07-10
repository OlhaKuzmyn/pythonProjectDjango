from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class UserModel(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table='aut'
