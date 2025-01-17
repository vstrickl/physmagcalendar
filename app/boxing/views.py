"""This Module creates the Boxing Page UI."""
# pylint: disable=no-member
from django.shortcuts import render

from home.models import GymInfo

# Create your views here.

def boxing(request):
    """Renders the Boxing Calendar."""
    title = 'Boxing'

    gym_info = GymInfo.objects.get(pk=1)

    context = {
        'title' : title,
        'g':gym_info,
        }

    return render(request, 'boxing.html', context)
