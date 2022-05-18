from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.relations import SlugRelatedField

from api_v1.models import Post, Follow, Readed


class FeedSerializer(serializers.ModelSerializer):
    """Сериализатор ленты, основанной на подписках на авторов."""
    author = SlugRelatedField(slug_field='username', read_only=True)
    
    class Meta:
        exclude = ('id',)
        model = Post


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор подписок на авторов."""
    
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


class AllPostsSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    
    class Meta:
        exclude = ('id',)
        model = Post


class UserBlogSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    
    def create(self, validated_data):
        user_id = (
            int(self.context.get('request')
            .parser_context.get('kwargs').get('user_id'))
        )
        author_id = int(validated_data.get('author').id)
        if user_id == author_id:
            post = Post.objects.create(**validated_data)
            return post
        else:
            raise ValidationError(
                {'error': 'Вы не можете оставлять записи в чужом блоге'}
            )
    
    class Meta:
        exclude = ('id',)
        model = Post
