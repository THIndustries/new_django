from django.core.management.base import BaseCommand
from myapp2.models import Author, Post


class Command(BaseCommand):
    help = 'Get post by author id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author id')

    # def handle(self, *args, **options):
    #     pk = options['pk']
    #     author = Author.objects.filter(pk=pk).first()
    #     if author is not None:
    #         posts = Post.objects.filter(author=author)# тут будет храниться
    #         # query set со всеми поставми автора
    #         intro = f'All posts of {author.name}\n'
    #         text = '\n'.join(post.content for post in posts)
    #         self.stdout.write(f'{intro}{text}')

    def handle(self, *args, **options):
        pk = options['pk']
        posts = Post.objects.filter(author__pk=pk) # проверяем соответствие столбца author_id
        # с аргументом что передали
        intro = f"All posts\n"
        text = '\n'.join(post.get_summary() for post in posts)
        self.stdout.write(f'{intro}{text}')