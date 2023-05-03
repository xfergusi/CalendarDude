import hashlib

from icalendar import Calendar, Event as calEvent
from BackEnd.Event import Event
import os


def set_id(summary, start, end):
    id_pre_hex = str(summary) + str(start) + str(end)
    id_pre_hex = id_pre_hex.encode('utf-8')
    return hashlib.sha256(id_pre_hex).hexdigest()


class EventManager:

    the_brain = []

    def make_an_all_day_event(self, summary, start, end):
        event_id = set_id(summary, start, end)
        self.the_brain.append(Event(event_id, summary, start, end))

    def make_an_event(self, summary, start, end):
        event_id = set_id(summary, start, end)
        self.the_brain.append(Event(event_id, summary, start, end))

    def make_the_ics_file(self):

        cal = Calendar()
        for event in self.the_brain:
            calevent = calEvent()
            calevent.add('summary', event.summary)
            calevent.add('description', event.description)
            calevent.add('dtstart', event.start)
            calevent.add('dtend', event.end)
            calevent['uid'] = event.event_id
            cal.add_component(calevent)

        f = open(os.path.join('example.ics'), 'wb')
        f.write(cal.to_ical())
        f.close()
