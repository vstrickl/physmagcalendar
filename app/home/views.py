from django.shortcuts import render

# Create your views here.

from .models import GymInfo
from boxing.models import BoxingClass
from fitness.models import FitnessClass
from oweightlifting.models import LiftingClass
from studio.models import StudioClass

def home(request):

    title = 'Schedule'

    gym_info = GymInfo.objects.get(pk=1)
    boxing = BoxingClass.objects.all()
    fitness = FitnessClass.objects.all()
    lifting = LiftingClass.objects.all()
    studio = StudioClass.objects.all()

    context = {
        'title':title,
        'g':gym_info,
        'boxing':boxing,
        'fitness':fitness,
        'lifting':lifting,
        'studio':studio,
    }
    return render(request, 'schedules.html', context)