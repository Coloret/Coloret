from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from accounts.models import UserProfile
from Posts.models import Post
# Create your models here.


class Comment(models.Model):

    user = models.ForeignKey(UserProfile)

    #Fields for a Generic Relation between Comment and other models
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # Fields for the actual comment attributes
    content = models.TextField
    published_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return str(self.user.username)