from django.core.management.base import BaseCommand
from myapp2.models import Post

class Command(BaseCommand):
    help = 'Delete post'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Post ID')

    def handle(self, *args, **options):
        post = Post.objects.filter(pk=options.get('pk')).first()
        if post is not None:
            post.delete()
            self.stdout.write('Post delete')
