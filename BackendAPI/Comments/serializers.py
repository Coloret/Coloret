from rest_framework import serializers, viewsets, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from Comments.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()