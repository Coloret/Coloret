from accounts.models import UserProfile
from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class UserSerializer(serializers.ModelSerializer):
    permission_classes = []
    class Meta:
        model = UserProfile
        fields = ('username', 'first_name', 'last_name', 'email', 'date_joined', 'password')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):

        " make sure to come back and edit this"
        "We can validate each field of the validated_data and " \
        "see if it has a value or not and then create a user object"
        user = UserProfile.objects.create(username = validated_data['username'],
                    email= validated_data['email'],
                    first_name = validated_data['first_name'],
                    last_name = validated_data['last_name'],
                    date_joined = validated_data['date_joined'],
                    )
        user.set_password(validated_data['password'])
        user.save()
        return user