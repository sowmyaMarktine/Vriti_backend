from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

class MyManager(BaseUserManager):
    def create_user(self, email, username, password = None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        # user.set_password(make_password(password))
        user.is_staff = True
        user.save()

        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        user.save()

        return user


categories = (
    ('employee', 'Employee'),
    ('employer', 'Employer'),
)

class User(AbstractBaseUser):
    username = models.CharField(max_length = 50)
    first_name = models.CharField(max_length = 50, blank = True)
    last_name = models.CharField(max_length = 50, blank = True)
    email = models.EmailField(unique = True)
    category = models.CharField(max_length = 30, choices = categories, default = 'employee')
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    is_admin = models.BooleanField(default = False)

    objects = MyManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'category']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj = None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        print('token generated')
        Token.objects.create(user=instance)
# class Category(models.Model):
#     # category_id = models.IntegerField(primary_key = True)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     category = models.CharField(max_length=50)

