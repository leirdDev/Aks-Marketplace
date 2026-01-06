from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
  first_name = models.CharField(max_length=150)
  last_name = models.CharField(max_length=150)
  profile_url = models.URLField(blank=True)

  REQUIRED_FIELDS = ["first_name", "last_name"]
