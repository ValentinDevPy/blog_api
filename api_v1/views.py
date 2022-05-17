from rest_framework import viewsets, mixins

from api_v1.models import Post, Follow, Readed
from api_v1.serializers import FeedSerializer, FollowSerializer, ReadedSerializer


class FeedViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FeedSerializer
    
    def get_queryset(self):
        user = self.request.user
        posts = (
            Post.objects.filter(author__following__user=user)
            .exclude(readed_post__user__exact=user)[:500]
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
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
