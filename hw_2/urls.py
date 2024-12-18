from django.urls import path
from . import views

urlpatterns = [
    path('', views.hw_2, name='home'),
    path('hw_2/', views.hw_2, name='hw_2'),
]