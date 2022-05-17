from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from api_v1.views import FeedViewSet, FollowViewSet

app_name = 'api_v1'

router = routers.DefaultRouter()

router.register(r'feed', FeedViewSet, basename='posts')
router.register(r'follow', FollowViewSet, basename='follows')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
