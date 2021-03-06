from __future__ import print_function

from datetime import datetime
from datetime import timedelta

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
from BackEnd.AuthorizationSteve import AuthorizationSteve

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


class EventGrabber:
    service = AuthorizationSteve().get_service()

    def get_events(self):
        try:
            # service = build('calendar', 'v3', credentials=AuthorizationSteve.check_creds())
            # service = AuthorizationSteve().get_service()

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
            print(now)
            print('Getting the upcoming events from my favorite calendars')
            cals_i_care_about = ['1nh3pmsfnovdchf203l6i8tbtbtms8eg@import.calendar.google.com', 'xfergusi@gmail.com']
            events_from_all_cals = []
            for cal in cals_i_care_about:
                events_result = self.service.events().list(calendarId=cal,
                                                           timeMin="2022-02-03T00:00:00.000000Z",
                                                           # timeMin=now,
                                                           timeMax="2022-02-03T23:59:59.999999Z",
                                                           maxResults=10, singleEvents=True,
                                                           orderBy='startTime').execute()
                events_from_all_cals.append(events_result.get('items', []))

            if not events_from_all_cals:
                print('No upcoming events found.')
                return

            # Prints the start and name of the next 10 events
            for events in events_from_all_cals:
                for event in events:
                    start = event['start'].get('dateTime', event['start'].get('date'))
                    print(start, event['summary'])

        except HttpError as error:
            print('An error occurred: %s' % error)

    def get_all_event_ids_after_yesterday(self):
        try:
            # Call the Calendar API
            now = (datetime.utcnow() - timedelta(days=1)).isoformat() + 'Z'  # 'Z' indicates UTC time
            # print('Getting the upcoming events from my favorite calendars')
            cals_i_care_about = ['1nh3pmsfnovdchf203l6i8tbtbtms8eg@import.calendar.google.com', 'xfergusi@gmail.com']
            events_from_all_cals = []
            for cal in cals_i_care_about:
                events_result = self.service.events().list(calendarId=cal,
                                                           timeMin=now,
                                                           singleEvents=True,
                                                           timeZone='Australia/Sydney',
                                                           orderBy='startTime').execute()
                events_from_all_cals.append(events_result.get('items', []))

            if not events_from_all_cals:
                print('No upcoming events found.')
                return

            event_ids = []
            for events in events_from_all_cals:
                for event in events:
                    start = event['start'].get('dateTime', event['start'].get('date'))
                    if 'id' in event:
                        event_ids.append(event['id'])
            return event_ids

        except HttpError as error:
            print('An error occurred: %s' % error)

