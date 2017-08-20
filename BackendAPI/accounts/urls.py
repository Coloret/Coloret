from django.conf.urls import url, include
from accounts.views import RegisterUser
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token



urlpatterns = [
    url(r'^signup$', RegisterUser.as_view(), name= 'register'),
    url(r'^auth/social/', include('rest_framework_social_oauth2.urls')),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/token/$', obtain_jwt_token),
    url(r'^auth/token-refresh/', refresh_jwt_token),
]