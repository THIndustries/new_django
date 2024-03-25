from django.core.management.base import BaseCommand
from gamesapp.models import CoinFlip

class Command(BaseCommand):
    help = 'Delete value from coinflif db'

    def handle(self, *args, **options):
        size = len(CoinFlip.objects.all())
        for i in range(size):
            CoinFlip.objects.first().delete()