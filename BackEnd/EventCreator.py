from googleapiclient.errors import HttpError
from icalendar import Calendar, Event as calEvent, vCalAddress, vText
from datetime import datetime, date
import hashlib
from BackEnd.Event import Event

import os


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

    def make_an_event(self, events):

        cal = Calendar()
        for event in events:
            calevent = calEvent()
            calevent.add('summary', event.summary)
            calevent.add('description', event.description)
            calevent.add('dtstart', event.start)
            calevent.add('dtend', event.end)
            calevent.add('color', 'tomato')
            calevent['uid'] = event.event_id
            cal.add_component(calevent)

        f = open(os.path.join('example.ics'), 'wb')
        f.write(cal.to_ical())
        f.close()
