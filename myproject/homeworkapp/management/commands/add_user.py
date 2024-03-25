from django.core.management.base import BaseCommand
from homeworkapp.models import User

class Command(BaseCommand):
    help = 'Add user to User hw table'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='User name')
        parser.add_argument('email', type=str, help='user email')
        parser.add_argument('phone', type=str, help='user phone number')
        parser.add_argument('address', type=str, help='user address')

    def handle(self, *args, **options):
        user = User(
            name=options.get('name'),
            email=options.get('email'),
            phone_number=options.get('phone'),
            address=options.get('address')
        )
        user.save()
        self.stdout.write(f'User added')


