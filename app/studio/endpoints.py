# endpoints.py
"""This module creates API Endpoints for the Google Calendars with streaming response"""
import json
from django.http import StreamingHttpResponse, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from googleapiclient.errors import HttpError
from .fetch_events import get_calendar_events

def stream_events(events_iterator):
    """Stream events as a JSON array"""
    yield '['
    first = True
    for event in events_iterator:
        if not first:
            yield ','
        else:
            first = False
        yield json.dumps(event, cls=DjangoJSONEncoder)
    yield ']'

def calendar_events(request, calendar_id): # pylint: disable=unused-argument
    """
    This function streams events from Google Calendar as a JSON response
    to reduce memory usage
    """
    try:
        events_iterator = get_calendar_events(calendar_id)
        response = StreamingHttpResponse(
            stream_events(events_iterator),
            content_type='application/json'
        )
        return response
        
    except HttpError as e:
        error_content = e.content.decode("utf-8") if hasattr(e, 'content') else str(e)
        return JsonResponse(
            {'error': 'Google Calendar API error', 'details': error_content},
            status=500
        )
    except ValueError as e:
        return JsonResponse(
            {'error': 'Invalid calendar ID', 'details': str(e)},
            status=400
        )
    except ConnectionError as e:
        return JsonResponse(
            {'error': 'Network error while accessing Google Calendar', 'details': str(e)},
            status=503
        )
    except Exception as e:  # pylint: disable=broad-exception-caught
        return JsonResponse(
            {'error': 'An unexpected error occurred', 'details': str(e)},
            status=500
        )
