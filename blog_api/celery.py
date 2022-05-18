from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab
from dotenv import load_dotenv

load_dotenv()

HOUR_OF_SENDING = int(os.getenv('HOUR_OF_SENDING'))
MINUTE_OF_SENDING = int(os.getenv('MINUTE_OF_SENDING'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_api.settings')

app = Celery('blog_api')

app.config_from_object(settings, namespace='CELERY')

app.conf.enable_utc = False

app.conf.update(timezone='Europe/Moscow')

app.conf.beat_schedule = {
    'send-mail-every-day': {
        'task': 'send_emails.tasks.send_mail_func',
        'schedule': crontab(hour=HOUR_OF_SENDING, minute=MINUTE_OF_SENDING),
    }
    
}

app.autodiscover_tasks()
