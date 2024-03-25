from random import choices

from django.core.management.base import BaseCommand
from myapp3.models import Author, Post

LOREM = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " \
        "Nam faucibus sit amet libero nec fermentum. " \
        "Pellentesque vitae elementum mauris. " \
        "Etiam id magna eget ex hendrerit volutpat." \
        "Nullam dignissim odio nulla, ut pellentesque nisl eleifend eget. " \
        "Quisque eu vehicula felis, id cursus urna. " \
        "Donec iaculis, metus consequat rutrum efficitur, massa lacus euismod arcu, " \
        "ut mattis tellus eros non est. " \
        "Maecenas porttitor, libero quis suscipit ultricies, " \
        "est nulla finibus justo, ac commodo nisi odio eget velit. " \
        "Orci varius natoque penatibus et magnis dis parturient montes, " \
        "nascetur ridiculus mus. Phasellus ac auctor sem."


class Command(BaseCommand):
    help = 'Generate fake authors and posts.'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='count of User')

    def handle(self, *args, **options):
        text = LOREM.split()
        count = options.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Author_{i}', email=f"mail{i}@mail.com")
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=f'Title-{j}',
                    content=" ".join(choices(text, k=64)),  # используя модуль choices берем
                    # 64 случайных слов из списка text и собираем обратно в строку.
                    author=author
                )
                post.save()
