from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from accounts.views import RegisterUser



urlpatterns = [
    url(r'^signup$', RegisterUser.as_view(), name= 'register'),
    url(r'^auth/social/', include('rest_framework_social_oauth2.urls')),
    url(r'^auth/get-token/', obtain_jwt_token),
]