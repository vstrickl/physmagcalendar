from django.urls import path

from . import views

app_name = 'fitness'

urlpatterns = [
    path('', views.fitness, name='fitness')
]