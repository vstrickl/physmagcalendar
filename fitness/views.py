from django.shortcuts import render
from django.conf import settings

# Create your views here.

def fitness(request):

    context = { 
        'title' : 'Fitness',
        'fitnessid' : settings.FITNESS_ID,
        'apikey' : settings.GOOGLE_API_KEY,
    }

    return render(request, 'fitness.html', context)