from __future__ import print_function

from datetime import datetime
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

    def get_events_by_date_range(self, start_date, end_date):
        print("searching start: " + start_date + " - end date: " + end_date)
        try:
            # Call the Calendar API
            now = datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
            print(now)
            a_string = start_date[:10] + "T" + start_date[11:] + ".000000Z"
            print(a_string)
            # nu_start = datetime.strptime(start_date+".000000", '%Y-%m-%d %H:%M:%S.%f')
            # print( nu_start )
            # print(datetime.strptime(now, '%Y-%m-%dT%H:%M:%S.%fZ'))
            print('Getting the upcoming events from my favorite calendars')
            cals_i_care_about = ['1nh3pmsfnovdchf203l6i8tbtbtms8eg@import.calendar.google.com', 'xfergusi@gmail.com']
            events_from_all_cals = []
            for cal in cals_i_care_about:
                events_result = self.service.events().list(calendarId=cal,
                                                           timeMin=a_string,
                                                           # timeMin=now,
                                                           # timeMax=end_date+'T23:59:59.999999Z',
                                                           maxResults=10, singleEvents=True,
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
                    print(start, event['summary'])
                    if 'description' in event:
                        event_ids.append(event['description'])
            print(event_ids)
            return event_ids

        except HttpError as error:
            print('An error occurred: %s' % error)

