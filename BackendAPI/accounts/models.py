from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(User):
    permission_classes = []
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "@{}".format(self.username)
