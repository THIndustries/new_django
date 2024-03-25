from django.core.management.base import BaseCommand
from myapp2.models import Author, Post


class Command(BaseCommand):
    help = 'Generate fake authors and posts.'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='How many User id create')

    def handle(self, *args, **options):
        count = options['count']
        for i in range(1, count + 1):
           author = Author(name=f'Name_{i}', email=f'mail_{i}.mail.com')
           author.save()
           for j in range(1, count + 1):
               post = Post(
                   title=f'Title_{j}',
                   content=f'Text from {author.name} #{j} and wery long text from this author.',
                   author=author
               )
               post.save()

