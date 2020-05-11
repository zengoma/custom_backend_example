from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="profile")
    approved = models.BooleanField(default=False)


class User(AbstractUser):
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.profile:
            Profile.objects.create(user=self)
