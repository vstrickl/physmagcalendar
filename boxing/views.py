from django.shortcuts import render
from django.conf import settings

from home.models import GymInfo

# Create your views here.

def boxing(request):

    title = 'Boxing'
    google_api_key = settings.GOOGLE_API_KEY
    boxing_calendar_id = settings.BOXING_CALENDAR_ID

    gym_info = GymInfo.objects.get(pk=1)

    context = { 
        'title' : title,
        'g':gym_info,
        'google_api_key':google_api_key,
        'boxing_calendar_id':boxing_calendar_id,
        }

    return render(request, 'boxing.html', context)
