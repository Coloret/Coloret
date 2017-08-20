from django.shortcuts import render
from rest_framework import generics
from accounts.serializers import UserSerializer
from django.contrib.auth import get_user_model

# Create your views here.

UserProfile = get_user_model()

class RegisterUser(generics.CreateAPIView):
    permission_classes = []

    " Create a new User"

    serializer_class = UserSerializer

    queryset = UserProfile.objects.all()