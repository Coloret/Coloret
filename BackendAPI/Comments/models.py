from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from accounts.models import UserProfile
from Posts.models import Post
# Create your models here.


class Comment(models.Model):

    user = models.ForeignKey(UserProfile)

    #Fields for a Generic Relation between Comment and Post
    post = models.ForeignKey(Post, related_name='comments')
    # Fields for the actual comment attributes
    content = models.TextField
    published_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return str(self.user.username)

    def get_comment_content(self):
        return self.content