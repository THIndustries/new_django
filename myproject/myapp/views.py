from django.shortcuts import render
from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page accessed')
    context = {'title': 'Index page', 'text': 'Текст для вывода через шаблонизатор в index.html'}
    return render(request, 'myapp/index.html', context)

def about(request):
    logger.debug('About page accessed')
    context = {'title': 'Index page', 'text': 'Текст для вывода через шаблонизатор в About.html'}
    return render(request, 'myapp/About.html', context)