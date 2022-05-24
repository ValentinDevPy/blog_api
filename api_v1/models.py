from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import UniqueConstraint

User = get_user_model()


class Post(models.Model):
    """Модель, описывающая посты пользователей."""
    header = models.CharField(
        'Заголовок поста',
        help_text='Введите заголовок поста',
        max_length=30,
    )
    text = models.TextField(
        'Текст поста',
        help_text='Введите текст поста',
        max_length=140,
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор',
    )
    
    def __str__(self) -> str:
        return str(self.text[:15])
    
    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Follow(models.Model):
    """Модель, описывающая подсписки пользователей
    друг на друга.
    """
    user = models.ForeignKey(
        User,
        related_name='follower',
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        User,
        related_name='following',
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return f'Пользователь {self.user}подписан на автора{self.author}'
    
    class Meta:
        verbose_name = 'Пользователь подписан на блог'
        verbose_name_plural = 'Пользователи подписаны на блоги'
        constraints = [UniqueConstraint(
            fields=['user', 'author'],
            name='unique_follow',
        )]


class Readed(models.Model):
    """Модель, описывающая прочтенные каждым пользователем посты."""
    user = models.ForeignKey(
        User,
        related_name='user_readed_post',
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        Post,
        related_name='readed_post',
        on_delete=models.DO_NOTHING,
    )
    
    def __str__(self):
        return f'Пользователь {self.user} прочитал пост {self.post.text[:15]}'
    
    class Meta:
        verbose_name = 'Прочитанный пост'
        verbose_name_plural = 'Прочитанные посты'
        constraints = [UniqueConstraint(
            fields=['user', 'post'],
            name='unique_readed',
        )]

