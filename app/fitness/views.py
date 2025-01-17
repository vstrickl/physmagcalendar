"""This Module creates the Fitness Page UI."""
# pylint: disable=no-member
from django.shortcuts import render

from home.models import GymInfo

# Create your views here.

def fitness(request):
    """This function renders the fitness page."""
    title = 'Fitness'

    gym_info = GymInfo.objects.get(pk=1)

    context = {
        'title' : title,
        'g':gym_info,
    }

    return render(request, 'fitness.html', context)
