from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
from AuthorizationSteve import AuthorizationSteve

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


class EventGrabber:
    @staticmethod
    def get_events():
        try:
            service = build('calendar', 'v3', credentials=AuthorizationSteve.check_creds())

            # page_token = None
            # while True:
            #     calendar_list = service.calendarList().list(pageToken=page_token).execute()
            #     for calendar_list_entry in calendar_list['items']:
            #         print(calendar_list_entry)
            #     page_token = calendar_list.get('nextPageToken')
            #     if not page_token:
            #         break

            # Call the Calendar API
            now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
            print('Getting the upcoming events from my favorite calendars')
            calsICareAbout = ['1nh3pmsfnovdchf203l6i8tbtbtms8eg@import.calendar.google.com', 'xfergusi@gmail.com']
            eventsFromAllCals = []
            for cal in calsICareAbout:
                events_result = service.events().list(calendarId=cal, timeMin=now,
                                                      maxResults=10, singleEvents=True,
                                                      orderBy='startTime').execute()
                eventsFromAllCals.append(events_result.get('items', []))

            if not eventsFromAllCals:
                print('No upcoming events found.')
                return

            # Prints the start and name of the next 10 events
            for events in eventsFromAllCals:
                for event in events:
                    start = event['start'].get('dateTime', event['start'].get('date'))
                    print(start, event['summary'])

        except HttpError as error:
            print('An error occurred: %s' % error)
