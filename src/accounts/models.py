from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    last_visit = models.DateTimeField(null=True)
