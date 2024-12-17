from django.urls import path
from main.views import main, list

urlpatterns = [
    path('', main, name='main'),
    path('list/', list, name='list')
]

