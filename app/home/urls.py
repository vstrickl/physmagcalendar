"""This is a module for the URL Path for this Project."""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home')
]
