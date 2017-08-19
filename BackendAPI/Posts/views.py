from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from Posts.serializers import PostSerializers
from Posts.models import Post
# Create your views here.

class PostViewset(ModelViewSet):
    serializer_class = PostSerializers
    queryset = Post.objects.all()