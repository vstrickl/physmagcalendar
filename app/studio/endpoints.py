"""This module creates API Endpoints for the Google Calendars"""

from django.http import JsonResponse
from googleapiclient.errors import HttpError
from .fetch_events import get_calendar_events

def calendar_events(request, calendar_id): # pylint: disable=unused-argument
    """
    This function fetches events from a
    Google Calendar and returns them as a JSON response
    """
    try:
        events = get_calendar_events(calendar_id)
        return JsonResponse(events, safe=False)
    except HttpError as e:  # Specific exception for Google API errors
        error_content = e.content.decode("utf-8") if hasattr(e, 'content') else str(e)
        return JsonResponse(
            {'error': 'Google Calendar API error', 'details': error_content},
            status=500
        )
    except ValueError as e:  # Handles invalid calendar_id or data type errors
        return JsonResponse(
            {'error': 'Invalid calendar ID', 'details': str(e)},
            status=400
        )
    except ConnectionError as e:  # Handles network issues
        return JsonResponse(
            {'error': 'Network error while accessing Google Calendar', 'details': str(e)},
            status=503
        )
    except Exception as e:  # pylint: disable=broad-exception-caught
        return JsonResponse(
            {'error': 'An unexpected error occurred', 'details': str(e)},
            status=500
        )
