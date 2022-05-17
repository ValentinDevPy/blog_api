from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from api_v1.models import Post


class FeedSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    
    class Meta:
        exclude = ('id',)
        model = Post
