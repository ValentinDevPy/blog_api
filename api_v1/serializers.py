from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from api_v1.models import Post, Follow


class FeedSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    
    class Meta:
        exclude = ('id',)
        model = Post


class FollowSerializer(serializers.ModelSerializer):
    
    class Meta:
        exclude = ('id', 'user')
        model = Follow
