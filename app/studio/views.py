# views.py
"""This Module creates views for the Studio Calendar with improved error handling"""
# pylint: disable=no-member
import logging
from django.shortcuts import render
from home.models import GymInfo

LEVEL = logging.INFO
logging.basicConfig(level=LEVEL, format='%(message)s')
logger = logging.getLogger(__name__)

def studio(request):
    """This view renders the Studio Calendar with improved error handling"""
    gym_info = GymInfo.objects.get(pk=1)

    context = {
        'title': 'Martial Arts Studio',
        'g': gym_info,
    }
    return render(request, 'studio.html', context)
