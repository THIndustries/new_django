from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    heplp = 'Get all users.'

    def handle(self, *args, **kwargs):
        users = User.objects.all() # objects в данном контексте означает, что я обращаюсь к
        # записям, строкам в базе данных. Из таблицы User обратись к строкам и верни всё.
        self.stdout.write(f'{users}')
