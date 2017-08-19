from rest_framework import serializers
from Posts.models import Post
from Comments.models import Comment

class PostSerializers(serializers.ModelSerializer):

    content = serializers.CharField(source='Comment.get_content_comment', read_only=True)
    class Meta:

        model = Post
        fields = [
            'user',
            'publish_date',
            'content',
        ]