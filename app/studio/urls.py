"""This module creates URL Path for the Studio app."""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.studio, name='studio'),
]
