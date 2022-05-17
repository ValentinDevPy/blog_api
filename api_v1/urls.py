from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from api_v1.views import (
    FeedViewSet, FollowViewSet,
    ReadedViewSet, AllPostsViewSet, UserBlogViewSet
)

app_name = 'api_v1'

router = routers.DefaultRouter()

router.register(r'feed', FeedViewSet, basename='feed')
router.register(r'posts', AllPostsViewSet, basename='posts')
router.register(r'blog/(?P<user_id>\d+)', UserBlogViewSet, basename='blogs')
router.register(r'readed', ReadedViewSet, basename='readed')
router.register(r'follow', FollowViewSet, basename='follows')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
