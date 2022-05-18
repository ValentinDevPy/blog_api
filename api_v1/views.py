import os

from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from api_v1.models import Post, Follow, Readed
from api_v1.serializers import (
    FeedSerializer, FollowSerializer,
    ReadedSerializer, AllPostsSerializer, UserBlogSerializer
)

POSTS_ON_FEED_PAGE = int(os.getenv('POSTS_ON_FEED_PAGE'))


class FeedViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """Логика работы ленты постов от авторов,
    на которых подписан пользователь.
    """
    serializer_class = FeedSerializer
    
    def get_queryset(self):
        user = self.request.user
        posts = (
            Post.objects.filter(author__following__user=user)
            .exclude(readed_post__user__exact=user)[:POSTS_ON_FEED_PAGE]
        )
        return posts


class FollowViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    """Логика работы подписок. Можно как посмотреть свои подписки('GET'),
    так и подписаться на пользователя по его id ('POST')."""
    
    serializer_class = FollowSerializer
    
    def get_queryset(self):
        user = self.request.user
        follows = Follow.objects.filter(user=user)
        return follows
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReadedViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """ Можно пометить пост как прочитанный по его id ('POST')."""
    
    serializer_class = ReadedSerializer
    permission_classes = (IsAuthenticated,)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AllPostsViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """Просмотр всей ленты новостей, отсюда тоже можно созать новый пост."""
    
    queryset = Post.objects.all()
    serializer_class = AllPostsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserBlogViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    """Переход на блог конкретного пользователя со всеми его постами.
    Если находишься в своем блоге - можешь так же создать новую запись.
    """
    serializer_class = UserBlogSerializer
    permission_classes = (IsAuthenticated,)
    ordering = ['-pub_date']
    
    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        posts = Post.objects.filter(author=user_id)
        return posts
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
