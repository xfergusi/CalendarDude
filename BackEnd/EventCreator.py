from googleapiclient.errors import HttpError
from icalendar import Calendar, Event, vCalAddress, vText
from datetime import datetime, date
import hashlib

import os
import pytz

from BackEnd.AuthorizationSteve import AuthorizationSteve


class EventCreator:
    def __make_an_event_direct_to_gcal(self, event_id, summary, description, start, end, allday):
        time_period = "dateTime"
        if allday:
            time_period = "date"
            start = start[0:10]
            end = end[0:10]
        event = {
            'summary': summary,
            'description': description,
            'id': event_id,
            'start': {
                time_period: start,
                'timeZone': 'Australia/Sydney',
            },
            'end': {
                time_period: end,
                'timeZone': 'Australia/Sydney',
            },
        }

        service = AuthorizationSteve().get_service()
        try:
            event = service.events().insert(calendarId='primary', body=event).execute()
            print('Event created: %s' % (event.get('htmlLink')))
        except HttpError as error:
            if error.status_code == 409:
                print(error.reason + " This should be ok. I probably deleted something: " + start)
                pass

    def make_an_event_direct_to_gcal(self, event_id, summary, description, start, end):
        self.__make_an_event_direct_to_gcal(event_id, summary, description, start, end, False)

    def make_an_all_day_event_direct_to_gcal(self, event_id, summary, description, start, end):
        self.__make_an_event_direct_to_gcal(event_id, summary, description, start, end, True)


    def __make_an_event_in_ics(self, event_id, summary, description, start, end, allday):

        cal = Calendar()
        event = Event()
        event.add('summary', summary)
        event.add('description', description)
        event.add('dtstart', date(2023, 1, 25))
        event['uid'] = event_id

        cal.add_component(event)

        event = Event()
        event.add('summary', 'testing please work')
        event.add('description', 'something')
        event.add('dtstart', date(2023, 1, 26))
        event['uid'] = event_id

        cal.add_component(event)

        f = open(os.path.join('example.ics'), 'wb')
        f.write(cal.to_ical())
        f.close()