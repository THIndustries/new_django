from django.core.management.base import BaseCommand
from myapp2.models import User, Product
from random import uniform

class Command(BaseCommand):
    help = 'Create content for Products table'

    def handle(self, *args, **options):
        PRODUCTS = [
            'Картофель', 'Морковь', 'Лук', 'Чеснок', 'Петрушка', 'Укроп', 'Яблоки', 'Бананы', 'Лимон',
            'Масло сливочное', 'Кефир', 'Молоко', 'Сметана', 'Творог', 'Сыр',
            'Горчица', 'Малиновое варенье', 'Томатная паста', 'Рыбная консерва', 'Консервированный горошек',
            'Консервированная кукуруза', 'Сгущенка', 'Мед',
        ]
        while PRODUCTS:
            product_name = PRODUCTS.pop()
            product = Product(
                name=product_name,
                price=round(uniform(10, 100), 2),
                description=f'Описание для {product_name}',
                image='image'
            )
            product.save()
        self.stdout.write(f'Done...')