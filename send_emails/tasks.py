import os

from api_v1.models import User, Post

from celery import shared_task
from django.core.mail import send_mail
from blog_api import settings

NUMBER_OF_POSTS_IN_EMAIL = int(os.getenv('NUMBER_OF_POSTS_IN_EMAIL'))


@shared_task(bind=True)
def send_mail_func(self):
    users = User.objects.all()
    for user in users:
        mail_subject = "Latest posts"
        posts = (
            Post.objects.filter(author__following__user=user)
            .exclude(readed_post__user__exact=user)[:NUMBER_OF_POSTS_IN_EMAIL]
        )
        posts_text = [f'Text: {post.text} Author: {post.author}' for post in posts]
        posts_text = '\n'.join(posts_text)
        message = posts_text
        to_email = user.email
        if message:
            send_mail(
                subject=mail_subject,
                message=message,
                from_email=settings.EMAIL_ADMIN,
                recipient_list=[to_email],
                fail_silently=True,
            )
    return "Done"
