from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth import get_user_model

class User(AbstractUser):
    is_buyer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
class Buyer(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)


class Seller(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)