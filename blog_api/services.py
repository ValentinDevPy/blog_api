from rest_framework.generics import get_object_or_404

from api_v1.models import Post


def get_posts(self):
    user_id = self.kwargs.get('user_id')
    posts = Post.objects.filter(author=user_id)
    return posts
