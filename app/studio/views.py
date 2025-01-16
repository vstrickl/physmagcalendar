"""This Module creates views for the Studio Calendar."""
# pylint: disable=no-member

import logging
from django.http import HttpResponseServerError
from django.shortcuts import render
from django.conf import settings

from home.models import GymInfo
from .parse_vite import get_vite_asset_path

LEVEL = logging.INFO
logging.basicConfig(level=LEVEL, format='%(message)s')
logger = logging.getLogger(__name__)

# Create your views here.
def studio(request):
    """This view renders the Studio Calendar."""
    try:
        gym_info = GymInfo.objects.get(pk=1)
        if not settings.STUDIO_CALENDAR_ID or not settings.VONS_PRIVATES_ID:
            logger.info("Calendar IDs are not configured")
            raise ValueError("Calendar IDs are not configured")
        context = {
            'title': 'Martial Arts Studio',
            'g': gym_info,
            'studio_calendar': settings.STUDIO_CALENDAR_ID,
            'vons_privates': settings.VONS_PRIVATES_ID,
            'studio_js': get_vite_asset_path('studio.jsx')
        }
        return render(request, 'studio.html', context)
    except GymInfo.DoesNotExist:
        logger.info("Calendar IDs are not configured")
        return HttpResponseServerError("GymInfo not found.")
    except ValueError as e:
        logger.info("Server/Value Error: %s", e)
        return HttpResponseServerError(str(e))
