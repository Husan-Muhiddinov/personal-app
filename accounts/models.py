from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.


class CustomUser(AbstractUser):
    age=models.PositiveIntegerField(null=True, blank=True)    # null=True, blank=True  yoshini so'rash shart emasligi uchun true