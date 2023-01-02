from django.urls import path

from . import views

app_name = 'oweightlifting'

urlpatterns = [
    path('', views.lift, name='lift')
]