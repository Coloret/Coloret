from accounts.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model

UserProfile = get_user_model()
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):

        " make sure to come back and edit this"
        "We can validate each field of the validated_data and " \
        "see if it has a value or not and then create a user object"
        user = UserProfile.objects.create(username = validated_data['username'],
                    email= validated_data['email'],
                    first_name = validated_data['first_name'],
                    last_name = validated_data['last_name'],
                    )
        user.set_password(validated_data['password'])
        user.save()
        return user