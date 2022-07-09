from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import datetime

# Create your models here.
class accountmanager(BaseUserManager):
    def create_user(self, username, password, NAME="", photo="", balance=0, SEM="", DEPT="", TE=0, is_faculty="False", is_student="True", is_merchant="False", is_office="False"):
        if not username:
            raise ValueError("username required")

        user = self.model(
            username = username,
            NAME=NAME,
            balance=balance,
            SEM=SEM,
            DEPT=DEPT,
            TE=TE,
            photo=photo,

            is_faculty=is_faculty,
            is_student=is_student,
            is_merchant=is_merchant,
            is_office=is_office
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            password = password,
            username = username,
        )
        user.is_admin = True
        user.is_faculty = True
        user.is_merchant = True
        user.is_student = True
        user.is_office = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class account(AbstractBaseUser):

    NAME = models.CharField(max_length=30)
    SEM = models.CharField(max_length=20)
    DEPT = models.CharField(max_length=100)
    balance = models.IntegerField(default=0, null=True)
    TE = models.IntegerField(default=0, null=True)
    photo = models.CharField(max_length=200)
    username = models.CharField(max_length=30, unique=True)
    is_admin = models.BooleanField(default=False)
    is_faculty = models.BooleanField(default=False)
    is_merchant = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_office = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    objects = accountmanager()

    def __str__(self):
        return self.username

    def has_perm(self , perm , obj = None):
        return self.is_admin

    def has_module_perms(self , app_label ):
        return True
