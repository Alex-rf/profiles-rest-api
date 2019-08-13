from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
#CREAT USER MANAGER.
class UserProfileManager(BaseUserManager):
    """ manager for user proiles"""

    def create_user(self, email, name, password=None):
        """ create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email,name, password):
        user= self.create_user(email, name, password)

        user.is_staff = True
        user.is_superuser= True
        user.save(using=self._db)

        return user


#creating the django models
class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=225, unique=True)
    name = models.CharField(max_length=225, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objectcs = UserProfileManager()


    USERNAME_FIELD = 'email'
    REQUIRES_FIELD = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.name
