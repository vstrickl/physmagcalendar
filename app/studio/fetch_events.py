# fetch_events.py
"""This module fetches events from Google Calendar with memory optimizations"""
from datetime import datetime, timedelta
from typing import Iterator, Dict, Any
from django.conf import settings
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

SERVICE_ACCOUNT_FILE = settings.GOOGLE_CREDS
SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_date_range():
    """Calculate and return the date range for calendar events"""
    today = datetime.now()
    monday = today - timedelta(days=today.weekday())
    start_date = monday.replace(hour=0, minute=0, second=0, microsecond=0)
    end_date = start_date + timedelta(weeks=4)

    return (
        start_date.isoformat() + 'Z',  # time_min
        end_date.isoformat() + 'Z'     # time_max
    )

def get_calendar_events(calendar_id: str) -> Iterator[Dict[str, Any]]:
    """
    Fetches events from Google Calendar using pagination and streaming
    Returns an iterator of events to reduce memory usage
    """
    credentials = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=SCOPES
    )

    service = build('calendar', 'v3', credentials=credentials)
    time_min, time_max = get_date_range()

    # Initialize the page token
    page_token = None

    while True:
        # Fetch events page by page
        events_result = service.events().list(  # pylint: disable=no-member
            calendarId=calendar_id,
            timeMin=time_min,
            timeMax=time_max,
            maxResults=250,  # Reduced from 2500 to handle smaller chunks
            pageToken=page_token,
            singleEvents=True,
            orderBy='startTime'
        ).execute()

        # Yield events one by one instead of collecting them
        for event in events_result.get('items', []):
            # Only yield necessary fields to reduce memory usage
            yield {
                'id': event.get('id'),
                'summary': event.get('summary'),
                'start': event.get('start'),
                'end': event.get('end'),
                'status': event.get('status'),
                # Add other essential fields as needed
            }

        # Get next page token
        page_token = events_result.get('nextPageToken')
        if not page_token:
            break
