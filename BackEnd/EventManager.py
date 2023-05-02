import hashlib

from BackEnd.Event import Event
from BackEnd.EventIDHolder import EventIDHolder


def set_id(summary, start, end):
    id_pre_hex = str(summary) + str(start) + str(end)
    id_pre_hex = id_pre_hex.encode('utf-8')
    return hashlib.sha256(id_pre_hex).hexdigest()


class EventManager:

    def __init__(self):
        self.event_id_holder = EventIDHolder()

    def make_an_all_day_event(self, summary, start, end):
        event_id = set_id(summary, start, end)
        if not self.check_if_event_exists(event_id):
            Event(event_id, summary, start, end).make_an_all_day_event_direct_to_gcal()

    def make_an_event(self, summary, start, end):
        event_id = set_id(summary, start, end)
        if not self.check_if_event_exists(event_id):
            Event(event_id, summary, start, end).make_an_event_direct_to_gcal()

    def check_if_event_exists(self, event_id):
        if event_id in self.event_id_holder.event_ids:
            print("Looks like this event already exists. I won't create another one. You're welcome ")
            return True

    def make_an_all_day_event(self, summary, start, end, input_method):
        event_id = set_id(summary, start, end)
        if input_method == "ics":
            Event(event_id, summary, start, end).make_an_all_day_event_direct_to_gcal()
        else:
            if not self.check_if_event_exists(event_id):
                Event(event_id, summary, start, end).make_an_all_day_event_direct_to_gcal()

    def make_an_event(self, summary, start, end, input_method):
        event_id = set_id(summary, start, end)
        if not self.check_if_event_exists(event_id):
            Event(event_id, summary, start, end).make_an_event_direct_to_gcal()
