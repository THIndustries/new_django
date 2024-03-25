from django.urls import path
from .views import coin, dice, randnums, index

urlpatterns = [
    path('', index, name='index'),
    path('coin/', coin, name='coin'),
    path('coin/<int:amount_flips>', coin, name='coin'),
    path('dice/', dice, name='dice'),
    path('randnums/', randnums, name='randnums'),
]

