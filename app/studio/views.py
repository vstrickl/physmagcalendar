# views.py
"""This Module creates views for the Studio Calendar with improved error handling"""
import logging
from django.http import HttpResponseServerError
from django.shortcuts import render
from django.conf import settings
from django.core.cache import cache
from home.models import GymInfo
from .parse_vite import get_vite_asset_path

LEVEL = logging.INFO
logging.basicConfig(level=LEVEL, format='%(message)s')
logger = logging.getLogger(__name__)

CACHE_TIMEOUT = 300  # 5 minutes cache

def get_gym_info():
    """Get gym info with caching"""
    cache_key = 'gym_info'
    gym_info = cache.get(cache_key)

    if gym_info is None:
        try:
            gym_info = GymInfo.objects.get(pk=1)  # pylint: disable=no-member
            cache.set(cache_key, gym_info, CACHE_TIMEOUT)
        except GymInfo.DoesNotExist:  # pylint: disable=no-member
            logger.error("GymInfo not found")
            return None

    return gym_info

def studio(request):
    """This view renders the Studio Calendar with improved error handling"""
    try:
        gym_info = get_gym_info()
        if gym_info is None:
            return HttpResponseServerError("GymInfo not found.")

        if not all([settings.STUDIO_CALENDAR_ID, settings.VONS_PRIVATES_ID]):
            logger.error("Calendar IDs are not configured")
            raise ValueError("Calendar IDs are not configured")

        context = {
            'title': 'Martial Arts Studio',
            'g': gym_info,
            'studio_calendar': settings.STUDIO_CALENDAR_ID,
            'vons_privates': settings.VONS_PRIVATES_ID,
            'studio_js': get_vite_asset_path('studio.jsx')
        }
        return render(request, 'studio.html', context)

    except ValueError as e:
        logger.error("Configuration error: %s", str(e))
        return HttpResponseServerError(str(e))
    except Exception as e:  # pylint: disable=broad-except
        logger.error("Unexpected error in studio view: %s", str(e))
        return HttpResponseServerError("An unexpected error occurred.")
