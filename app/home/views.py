"""This Module creates the Home Page UI view."""
# pylint: disable=no-member

from django.shortcuts import render

from boxing.models import BoxingClass
from fitness.models import FitnessClass
from oweightlifting.models import LiftingClass
from studio.models import StudioClass

# Create your views here.
def home(request):
    """This function renders the home page."""
    boxing = BoxingClass.objects.all()
    fitness = FitnessClass.objects.all()
    lifting = LiftingClass.objects.all()
    studio = StudioClass.objects.all()

    context = {
        'title':'Schedule',
        'boxing':boxing,
        'fitness':fitness,
        'lifting':lifting,
        'studio':studio,
    }
    return render(request, 'schedules.html', context)
