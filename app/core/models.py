from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, 
                                         PermissionsMixin)


class UserManager(BaseUserManager):
    """Manager class for user objects"""
    def create_user(self, email, password=None, **extra_fields):
        """Creates and save new user"""
        if not email:
            raise ValueError('user must have an email')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """Create super user using cretae user function"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    """Custom user that support emial instead of username"""
    email = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'