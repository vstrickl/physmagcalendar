"""This module creates URL Path for the Studio app."""
from django.urls import path

from . import views, endpoints

urlpatterns = [
    path('', views.studio, name='studio'),
    path(
        '/api/calendar/<str:calendar_id>/',
        endpoints.calendar_events,
        name='studio_calendar_events'
    ),
]
