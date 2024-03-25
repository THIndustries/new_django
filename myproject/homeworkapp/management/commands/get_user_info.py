from django.core.management.base import BaseCommand
from homeworkapp.models import User


class Command(BaseCommand):
    help = 'Get user info by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User id')

    def handle(self, *args, **options):
        user = User.objects.filter(pk=options.get('pk')).first()
        if user:
            self.stdout.write(f'{user}')
        else:
            self.stdout.write(f'User with this: {options["pk"]} id is not found')