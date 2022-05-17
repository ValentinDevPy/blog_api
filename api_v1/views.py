from rest_framework import viewsets

from api_v1.models import Post, Follow
from api_v1.serializers import FeedSerializer, FollowSerializer


class FeedViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FeedSerializer
    
    def get_queryset(self):
        user = self.request.user
        posts = Post.objects.filter(author__following__user=user)[:500]
        return posts


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
