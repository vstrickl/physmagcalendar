from django.shortcuts import render
from django.conf import settings

# Create your views here.
from home.models import GymInfo

def lift(request):

    title = 'Olympic Weightlifting'
    google_api_key = settings.GOOGLE_API_KEY
    oweightlifting_calendar_id = settings.OWEIGHTLIFTING_CALENDAR_ID

    gym_info = GymInfo.objects.get(pk=1)

    context = { 
        'title' : title,
        'g':gym_info,
        'google_api_key':google_api_key,
        'oweightlifting_calendar_id':oweightlifting_calendar_id,
        }
    
    return render(request, 'lift.html', context)