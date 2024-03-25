from django.core.management.base import BaseCommand
from myapp2.models import User, Product, Order
from random import choice
from datetime import datetime

class Command(BaseCommand):
    help = "Create orders"

    def handle(self, *args, **options):
        for i in range(1, 6):
            user = User.objects.get(pk=i)
            for j in range(1,4):
                product = choice(Product.objects.all())
                order = Order(
                    customer=user.id,
                    product=product,
                    date_ordered=datetime.now(),
                    total_price=product.price,
                )
                order.save()
            self.stdout.write('Done...')


