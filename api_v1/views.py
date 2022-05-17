from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from api_v1.models import Post
from api_v1.serializers import FeedSerializer


class FeedViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = FeedSerializer
    pagination_class = PageNumberPagination
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
