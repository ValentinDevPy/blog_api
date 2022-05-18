from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_api.settings')

app = Celery('blog_api')
app.conf.enable_utc = False
app.conf.update(timezone='Europe/Moscow')

app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {
    'send-mail-every-day-at-8': {
        'task': 'send_emails.tasks.send_mail_func',
        'schedule': crontab(minute='*/1'),
    }
    
}

app.autodiscover_tasks()
