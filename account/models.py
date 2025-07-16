from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserAccountManager(BaseUserManager):
     
     def create_user(self, full_name, username, email, password=None):
         
        if not username:
            raise ValueError('User must have an unique username')
        
        if not email:
            raise ValueError('User must have an unique email address')
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            full_name = full_name,
        )

        user.is_active = True 

        user.set_password(password)
        user.save(using=self._db)
        return user
     

     def create_superuser(self, full_name, username, email, password):
        
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            full_name = full_name,
            password = password,
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True

        user.save(using=self._db)
        return user




class UserAccount(AbstractBaseUser):

    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=100, unique=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name', 'email']

    objects = UserAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True 
