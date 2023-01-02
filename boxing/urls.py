from django.urls import path

from . import views

app_name = 'boxing'

urlpatterns = [
    path('', views.boxing, name='boxing')
]