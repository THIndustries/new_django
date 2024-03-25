from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    heplp = 'Create user.'

    def handle(self, *args, **kwargs):
        #user = User(name='John', email='john@mail.com', password='secret', age=25)
        user = User(name='Tom', email='Tom@mail.com', password='secret', age=30)
        #user = User(name='Bob', email='Bob@mail.com', password='secret', age=35)
        user.save() # сохраняем ЭК
        self.stdout.write(f'{user}')