from django.urls import path

from . import views

urlpatterns = [
    path('', views.lift, name='lift')
]