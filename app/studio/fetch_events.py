"""This module fetches events from Google Calendar"""
# pylint: disable=no-member

from django.conf import settings
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

SERVICE_ACCOUNT_FILE =  settings.GOOGLE_CREDS
SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_calendar_events(calendar_id):
    """Fetches events from Google Calendar"""
    # Path to your service account key JSON file

    # Authenticate using the service account
    credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # Build the Google Calendar API service
    service = build('calendar', 'v3', credentials=credentials)

    # Fetch events from the specified calendar
    events_result = service.events().list(
        calendarId=calendar_id,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    events = events_result.get('items', [])
    return events
