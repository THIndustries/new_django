from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.user, name='user'),
    path('user/<int:user_id>/posts/', views.user_posts, name='user_posts'),
    path('post/<int:post_id>', views.post, name='post'),
    path('allusers/', views.show_user, name='show_user')
]