from django.shortcuts import render
from .models import Post, Author, User, Product
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


def user(request):
    return HttpResponse('This is myapp2/user page')

def user_posts(request, user_id):
    user = get_object_or_404(Author, pk=user_id)
    posts = Post.objects.filter(author=user_id)
    context = {
        'title': f'Show posts',
        'posts': posts,
        'author': user,
    }
    return render(request, 'myapp2/user_posts.html', context)


def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.views += 1
    post.save()
    context = {
        'post': post,
    }
    return render(request, 'myapp2/post.html', context)


def show_user(request):
    users = User.objects.all()

    context = {
        "title": 'Все пользователи',
        'users': users
    }
    return render(request, 'myapp2/all_users.html', context)