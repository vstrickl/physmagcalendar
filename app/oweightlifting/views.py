"""This Module creates the Weightlifting Page UI."""
# pylint: disable=no-member
from django.shortcuts import render

# Create your views here.
from home.models import GymInfo

def lift(request):
    """Renders Weightlifting page."""
    title = 'Olympic Weightlifting'

    gym_info = GymInfo.objects.get(pk=1)

    context = {
        'title' : title,
        'g':gym_info,
        }

    return render(request, 'lift.html', context)
