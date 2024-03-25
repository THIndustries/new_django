from django.core.management.base import BaseCommand
from myapp2.models import Post

class Command(BaseCommand):
    help = 'Get all posts by title name'

    def add_arguments(self, parser):
        parser.add_argument('title', type=str, help='Title')

    def handle(self, *args, **options):
        title = options['title']
        post = Post.objects.filter(title=title).first()
        self.stdout.write(f'{post}')