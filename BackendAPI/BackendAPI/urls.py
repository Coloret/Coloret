"""BackendAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers, serializers, viewsets, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


from Comments.serializers import CommentViewSet
from Posts.views import PostViewset

router = routers.DefaultRouter()
router.register(r'comments',CommentViewSet)
router.register(r'posts', PostViewset)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api/accounts/',include('accounts.urls', namespace='accounts')),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    url(r'^api/auth/',include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/auth/token/$', obtain_jwt_token),
    url(r'^api/auth/token-refresh/', refresh_jwt_token),
]
