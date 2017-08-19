from django.conf.urls import url, include
from accounts.views import RegisterUser



urlpatterns = [
    url(r'^signup$', RegisterUser.as_view(), name= 'register'),
    url(r'^auth/social/', include('rest_framework_social_oauth2.urls')),
]