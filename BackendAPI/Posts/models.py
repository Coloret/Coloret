from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from accounts.models import UserProfile
# Create your models here.

class Post(models.Model):

    user = models.ForeignKey(UserProfile)
    publish_date = models.DateField()

