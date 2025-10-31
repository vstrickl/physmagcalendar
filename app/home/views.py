"""This Module creates the Home Page UI view."""
# pylint: disable=no-member
from django.db import connections
from django.http import HttpResponse
from django.shortcuts import render
from django.db.utils import OperationalError

from .models import UploadFile, GymInfo

# Create your views here.
def home(request):
    """This function renders the home page."""

    # Fetch all uploaded files
    uploaded_files = UploadFile.objects.all()
    gym_info = GymInfo.objects.filter(is_active=True)

    context = {
        'uploaded_files': uploaded_files,
        'gym_info': gym_info
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
