from django.shortcuts import render
from django.conf import settings

from home.models import GymInfo

# Create your views here.

def fitness(request):

    title = 'Fitness'
    google_api_key = settings.GOOGLE_API_KEY
    fitness_calendar_id = settings.FITNESS_CALENDAR_ID

    gym_info = GymInfo.objects.get(pk=1)

    context = { 
        'title' : title,
        'g':gym_info,
        'google_api_key':google_api_key,
        'fitness_calendar_id':fitness_calendar_id,
    }

    return render(request, 'fitness.html', context)