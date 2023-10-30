from django.shortcuts import render
from django.conf import settings

from home.models import GymInfo

# Create your views here.

def studio(request):
    title = 'Martial Arts & Dance Studio'
    google_api_key = settings.GOOGLE_API_KEY
    studio_calendar_id = settings.STUDIO_CALENDAR_ID

    gym_info = GymInfo.objects.get(pk=1)


    context = { 
        'title' : title,
        'g':gym_info,
        'google_api_key':google_api_key,
        'studio_calendar_id':studio_calendar_id,
        }
    
    return render(request, 'studio.html', context)