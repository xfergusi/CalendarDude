# imports
from icalendar import Calendar, Event, vCalAddress, vText
from datetime import datetime, date
from pathlib import Path
import hashlib

import os
import pytz


class Testing2:
    def test(self):
        cal = Calendar()
        # Add subcomponents
        event = Event()
        event.add('summary', 'testing please work')
        event.add('description', 'something')
        event.add('dtstart', date(2023, 1, 25))
        # event.add('dtend', datetime(2023, 1, 24, 0, 0, 0, tzinfo=pytz.timezone('Australia/Sydney')))
        id_pre_hex = str('testing please work') + str('2022') + str(2022)
        id_pre_hex = id_pre_hex.encode('utf-8')
        x = hashlib.sha256(id_pre_hex).hexdigest()
        print(x)
        event['uid'] = x

        # Add the organizer
        # organizer = vCalAddress('MAILTO:jdoe@example.com')
        # Add parameters of the event
        # organizer.params['name'] = vText('John Doe')
        # organizer.params['role'] = vText('CEO')
        # event['organizer'] = organizer
        # event['location'] = vText('New York, USA')

        # event.add('priority', 5)
        # attendee = vCalAddress('MAILTO:rdoe@example.com')
        # attendee.params['name'] = vText('Richard Roe')
        # attendee.params['role'] = vText('REQ-PARTICIPANT')
        # event.add('attendee', attendee, encode=0)
        #
        # attendee = vCalAddress('MAILTO:jsmith@example.com')
        # attendee.params['name'] = vText('John Smith')
        # attendee.params['role'] = vText('REQ-PARTICIPANT')
        # event.add('attendee', attendee, encode=0)

        # Add the event to the calendar
        cal.add_component(event)

        event = Event()
        event.add('summary', 'testing please work')
        event.add('description', 'something')
        event.add('dtstart', date(2023, 1, 26))
        # event.add('dtend', datetime(2023, 1, 24, 0, 0, 0, tzinfo=pytz.timezone('Australia/Sydney')))
        id_pre_hex = str('testing please work') + str('2012') + str(2022)
        id_pre_hex = id_pre_hex.encode('utf-8')
        x = hashlib.sha256(id_pre_hex).hexdigest()
        print(x)
        event['uid'] = x

        cal.add_component(event)

        # Write to disk
        # directory = Path.cwd() / 'MyCalendar'
        # try:
        #     directory.mkdir(parents=True, exist_ok=False)
        # except FileExistsError:
        #     print("Folder already exists")
        # else:
        #     print("Folder was created")
        #
        f = open(os.path.join('example.ics'), 'wb')
        f.write(cal.to_ical())
        f.close()
# {
#             'summary': summary,
#             'description': description,
#             'id': event_id,
#             'start': {
#                 time_period: start,
#                 'timeZone': 'Australia/Sydney',
#             },
#             'end': {
#                 time_period: end,
#                 'timeZone': 'Australia/Sydney',
#             },
#         }