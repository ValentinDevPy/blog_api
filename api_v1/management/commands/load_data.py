from django.core.management.base import BaseCommand
from .services import get_users, get_posts, get_follows
from api_v1.models import User, Post, Follow


class Command(BaseCommand):
    """ Команда предназначена для импорта csv данных в БД"""
    
    def handle(self, *args, **options):
        if User.objects.count() == 0:
            User.objects.create_superuser('admin', 'admin@example.com', 'pass')
        else:
            print('Admin accounts can only be initialized if no Accounts exist')
        
        """ Импортируем пользователей в БД."""
        if User.objects.count() == 1:
            get_users(self)
        """Импортируем посты в БД."""
        if Post.objects.count() == 0:
            get_posts(self)
        """Подписываем тестового пользователя на 10 юзеров."""
        if Follow.objects.count() == 0:
            get_follows(self)
