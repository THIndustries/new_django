from django.core.management.base import BaseCommand
from homeworkapp.models import Product

class Command(BaseCommand):
    help = 'Add product to Product hw table'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Product name')
        parser.add_argument('description', type=str, help='Product description')
        parser.add_argument('price', type=float, help='Product price')
        parser.add_argument('amount', type=int, help='Product amount')

    def handle(self, *args, **options):
        product = Product(
            name=options.get('name'),
            description=options.get('description'),
            price=options.get('price'),
            amount=options.get('amount')
        )
        product.save()
        self.stdout.write(f'{product.name} is added')

