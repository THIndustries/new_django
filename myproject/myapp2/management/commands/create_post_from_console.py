from django.core.management.base import BaseCommand
from myapp2.models import Post, User, Author


class Command(BaseCommand):
    help = 'Create post'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=str, help='user id')
        parser.add_argument('title', type=str, help='title')
        parser.add_argument('content', type=str, help='content')
        parser.add_argument('is_published', type=bool, help='is_publ')
        parser.add_argument('views', type=int, help='count of views')


    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = Author.objects.filter(pk=pk).first()

        post = Post(
            author=user,
            title=kwargs['title'],
            content=kwargs['content'],
            is_published=kwargs['is_published'],
            views=kwargs['views']
        )
        post.save()
        self.stdout.write(f'{post}')