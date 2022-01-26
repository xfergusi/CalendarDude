from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


class EventGrabber:
    @staticmethod
    def get_events():
        """Shows basic usage of the Google Calendar API.
        Prints the start and name of the next 10 events on the user's calendar.
        """
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        try:
            service = build('calendar', 'v3', credentials=creds)

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
