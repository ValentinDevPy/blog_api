import os

from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from api_v1.models import Post, Follow, Readed
from api_v1.serializers import (
    FeedSerializer, FollowSerializer,
    ReadedSerializer, AllPostsSerializer, UserBlogSerializer
)

POSTS_ON_FEED_PAGE = int(os.getenv('POSTS_ON_FEED_PAGE'))


class FeedViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FeedSerializer
    
    def get_queryset(self):
        user = self.request.user
        posts = (
            Post.objects.filter(author__following__user=user)
            .exclude(readed_post__user__exact=user)[:POSTS_ON_FEED_PAGE]
        )
        return posts


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReadedViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Readed.objects.all()
    serializer_class = ReadedSerializer
    permission_classes = (IsAuthenticated,)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AllPostsViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Post.objects.all()
    serializer_class = AllPostsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserBlogViewSet(viewsets.ModelViewSet):
    serializer_class = UserBlogSerializer
    permission_classes = (IsAuthenticated,)
    ordering = ['-pub_date']
    
    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        posts = Post.objects.filter(author=user_id)
        return posts
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
