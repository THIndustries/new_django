from django.core.management.base import BaseCommand
from homeworkapp.models import Product


class Command(BaseCommand):
    help = 'Get product info by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product id')

    def handle(self, *args, **options):
        product = Product.objects.filter(pk=options['pk']).first()
        if product:
            self.stdout.write(f'{product}')
        else:
            self.stdout.write(f'product not found')