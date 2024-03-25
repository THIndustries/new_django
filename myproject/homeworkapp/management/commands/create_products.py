from django.core.management.base import BaseCommand
from homeworkapp.models import Product
from random import random, uniform, shuffle, randint

class Command(BaseCommand):
    help = 'Create product at hw table'

    PRODUCT = [
        'Картофель', 'Морковь', 'Лук', 'Чеснок', 'Петрушка', 'Укроп', 'Яблоки', 'Бананы',
        'Лимон', 'Масло сливочное', 'Кефир', 'Молоко', 'Сметана', 'Творог', 'Сыр',
        'Горчица', 'Малиновое варенье', 'Томатная паста', 'Рыбная консерва',
        'Консервированный горошек', 'Консервированная кукуруза', 'Сгущенка', 'Мед',
    ]

    def add_arguments(self, parser):
        parser.add_argument('how_much', type=int, help='How much product create')

    def handle(self, *args, **options):
        count = options.get('how_much')
        temp_list = self.PRODUCT.copy()
        shuffle(temp_list)
        if count < len(temp_list):
            for i in range(1, count+1):
                product = Product(
                    name=temp_list.pop(),
                    description=f'description for product{i}',
                    price=round(uniform(10, 100), 2),
                    amount=randint(5,20)
                )
                product.save()
            self.stdout.write('for is ended')
        else:
            self.stdout.write('Yor count value is bigger then 23')


