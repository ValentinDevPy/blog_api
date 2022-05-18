import csv
import os

from django.conf import settings
from pytz import timezone

from api_v1.models import User, Post, Follow, Readed

""" Основная логика команды load_data для импорта csv данных в БД"""


def get_users(self):
    file_path = os.path.join(
        settings.BASE_DIR, 'static', 'data', 'Users.csv')
    with open(file_path, encoding='utf-8') as f:
        reader = csv.reader(f)
        first_line = 1
        for row in reader:
            if first_line:
                first_line = 0
                continue
            _, created = User.objects.get_or_create(
                id=row[0],
                first_name=row[1],
                last_name=row[2],
                email=row[3],
                password=row[4],
                is_superuser=row[5],
                is_active=row[6],
                is_staff=row[7],
                username=row[8],
                date_joined=row[9]
            )


def get_posts(self):
    file_path = os.path.join(
        settings.BASE_DIR, 'static', 'data', 'Posts.csv')
    with open(file_path, encoding='utf-8') as f:
        reader = csv.reader(f)
        first_line = 1
        for row in reader:
            if first_line:
                first_line = 0
                continue
            _, created = Post.objects.get_or_create(
                id=row[0],
                header=row[1],
                text=row[2],
                pub_date=row[3],
                author_id=row[4],
            )


def get_follows(self):
    file_path = os.path.join(
        settings.BASE_DIR, 'static', 'data', 'Follow.csv')
    with open(file_path, encoding='utf-8') as f:
        reader = csv.reader(f)
        first_line = 1
        for row in reader:
            if first_line:
                first_line = 0
                continue
            _, created = Follow.objects.get_or_create(
                id=row[0],
                author_id=row[1],
                user_id=row[2],
            )
