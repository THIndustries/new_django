from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic import TemplateView
from .models import Author, Post

# get_object_or_404 - функци, которая позволяет обращаться к БД и возвращать оттуда какой-то
# обьект, а если получить не удалоть, то ошибка 404

def index(request):
    return render(request, 'myapp3/index.html')

def about(request):
    return render(request, 'myapp3/about.html')



def hello(request):
    return HttpResponse('Hello world from myapp3 function!')


class HelloView(View):  # Представление на основе класса
    def get(self, request):
        return HttpResponse('Hello world from myapp3 class!')


def year_post(request, year):  # Представление
    text = """
    ...
    """
    return HttpResponse(f"Posts from {year}<br>{text}")


class MonthPost(View):
    def get(self, request, year, month):
        text = """
        ...
        """
        return HttpResponse(f"Posts from {month}/{year}<br>{text}")


def post_detail(request, year, month, slug):
    ...
    post = {
        'year': year,
        'month': month,
        'slug': slug,
        'title': "Кто быстрее создает списки в Python, list() или []",
        'content': "В процессе написания очередной программый задумался на тем,"
                   "какой способ создания списков в Python работает быстрее..."
    }

    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})  # Возвращаем не html
    # страницу а Json обьект в браузер. json_dumps_params - указываем, что в этом json обьект
    # будет задействованы не только латинские символы. Теперь проблем с отображением кирилицы
    # не будет.


def my_view(request):  # Пердставление на основе функции
    """
    Функция возвращает обьект render - предназначенный для упрощенной разработки
    :param request:
    :return: request - обьект запроса от пользователя, и его же используем чтобы вернуть ответ.
    Далее указываем путь до шаблона, обрати внимаение, что папку templates мы не указываем, её
    django найдет сам.
    """
    context = {'name': 'John'}
    return render(request, 'myapp3/my_template.html', context)


class TemplIf(TemplateView):  # TemplateView = класс, который позволяет создавать представления,
    # как и View, но со своими особеностями.

    template_name = 'myapp3/templ_if.html'  # 1. указываем имя нужного шаблона.

    # template_name, это зарезервированное слово, которое будет искать django, чтобы
    # понять о каком шаблоне идет речь если мы хотим использовать представление на основе
    # класса TemplateView

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Обращаемся к родительскому шаблону и
        # извлекаем контекст из него, а потом добавляем в него свои данные:
        context['message'] = 'Привет, мир!'
        context['number'] = 5
        return context


def view_for(request):
    my_list = ['apple', 'banana', 'orange']
    my_dict = {
        'каждый': 'красный',
        'охотник': 'оранжевый',
        'желает': 'жёлтый',
        'знать': 'зелёный',
        'где': 'голубой',
        'сидит': 'синий',
        'фазан': 'фиолетовый',
    }
    context = {'my_list': my_list, 'my_dict': my_dict}
    return render(request, 'myapp3/templ_for.html', context)


def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id) # Найди мне автора, pk которого соответствует
    # тому что ввел в строке браузера пользователь
    posts = Post.objects.filter(author=author).order_by('-id')[:5]
    context = {'author': author, 'posts': posts}
    return render(request, 'myapp3/author_posts.html', context)


def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'myapp3/post_full.html', {"post": post})