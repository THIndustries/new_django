from django.shortcuts import render
from django.http import HttpResponse
from random import randint, choice
import logging
from .models import CoinFlip

logger = logging.getLogger(__name__)

def index(request):
    logger.debug('Main page is visited')
    return HttpResponse('<h1>This is a module with games.</h1>')

def coin(request, amount_flips):
    result = choice(["Орел", "Решка"])
    logger.debug(f'Coin side is {result}')
    CoinFlip(side=result).save()
    context = {
        'current_flip': result,
        'last_results': CoinFlip.get_last_flip(amount_flips),
        'title': 'coin',
        'game_name': 'Бросок монетки',
        'result': result,
    }
    #return HttpResponse(f'Бросаем монетку.<br>Сторона монетки: {result}')
    return render(request, 'gamesapp/result.html', context)

def dice(request):
    result = randint(1,6)
    logger.debug(f'Dice side is {result}')
    context = {'title': 'dice', 'game_name': 'Бросок кубика', 'result': result}
    return render(request, 'gamesapp/result.html', context)

def randnums(request):
    result = randint(1,100)
    logger.debug(f'Random number is {result}')
    context = {'title': 'randnums', 'game_name': 'Cлучайное число', 'result': result}
    return render(request, 'gamesapp/result.html', context)