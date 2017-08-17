from django.db import models
from django.contrib.auth.models import User, PermissionsMixin

# Create your models here.

class UserProfile(User, PermissionsMixin):

    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return "@{}".format(self.username)
