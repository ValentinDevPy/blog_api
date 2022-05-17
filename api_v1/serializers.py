from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.relations import SlugRelatedField

from api_v1.models import Post, Follow, Readed


class FeedSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    
    class Meta:
        exclude = ('id',)
        model = Post


class FollowSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        try:
            follow = Follow.objects.create(**validated_data)
        except IntegrityError:
            raise ValidationError(
                {'error': 'Вы уже подписаны на этого человека'}
            )
        return follow
    
    class Meta:
        exclude = ('id', 'user')
        model = Follow


class ReadedSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        try:
            readed = Readed.objects.create(**validated_data)
        except IntegrityError:
            raise ValidationError(
                {'error': 'Данный пост уже помечен как прочитанный'}
            )
        return readed
    
    class Meta:
        exclude = ('id', 'user')
        model = Readed
