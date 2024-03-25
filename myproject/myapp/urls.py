from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_myapp'), #name = будет полезно в шаблонах
    path('about/', views.about, name='about_myapp'),
]
