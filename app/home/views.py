"""This Module creates the Home Page UI view."""
# pylint: disable=no-member

from django.db import connections
from django.http import HttpResponse
from django.shortcuts import render
from django.db.utils import OperationalError

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

def healthcheck(request):  # pylint: disable=unused-argument
    """This function checks the database connection."""
    # Try to connect to the database
    try:
        connections['default'].ensure_connection()
        return HttpResponse("OK", status=200)
    except OperationalError:
        return HttpResponse("Database unavailable", status=503)
