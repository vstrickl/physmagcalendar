"""This module fetches events from Google Calendar"""
# pylint: disable=no-member

from datetime import datetime, timedelta
from django.conf import settings
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

SERVICE_ACCOUNT_FILE =  settings.GOOGLE_CREDS
SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_calendar_events(calendar_id):
    """Fetches events from Google Calendar"""
    # Authenticate using the service account
    credentials = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, 
        scopes=SCOPES
    )

    # Build the Google Calendar API service
    service = build('calendar', 'v3', credentials=credentials)

    # Get this Monday at midnight
    today = datetime.now()
    monday = today - timedelta(days=today.weekday())
    start_date = monday.replace(hour=0, minute=0, second=0, microsecond=0)

    # Get date 4 weeks from Monday
    end_date = start_date + timedelta(weeks=4)
    
    # Format dates for API
    time_min = start_date.isoformat() + 'Z'  # 'Z' indicates UTC
    time_max = end_date.isoformat() + 'Z'

    # Fetch events from the specified calendar
    events_result = service.events().list(
        calendarId=calendar_id,
        timeMin=time_min,
        timeMax=time_max,
        maxResults=2500,  # Google Calendar API limit is 2500
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])
    return events
