import hashlib

from BackEnd.EventCreator import EventCreator
from BackEnd.EventIDHolder import EventIDHolder


def set_id(summary, start, end):
    id_pre_hex = str(summary) + str(start) + str(end)
    id_pre_hex = id_pre_hex.encode('utf-8')
    return hashlib.sha256(id_pre_hex).hexdigest()


class Event:
    event_id = None
    summary = None
    description = ""
    start = None
    end = None
    event_id_holder = None

    def __init__(self, summary, start, end):
        self.event_id_holder = EventIDHolder()
        self.event_id = set_id(summary, start, end)
        self.summary = summary
        self.start = str(start)
        self.end = str(end)

    def make_an_all_day_event(self):
        if not self.check_if_event_exists():
            EventCreator().make_an_all_day_event(self.event_id, self.summary, self.description, self.start, self.end)

    def make_an_event(self):
        if not self.check_if_event_exists():
            print("making an event for this time: " + self.start + " - " + self.end)
            EventCreator().make_an_event(self.event_id, self.summary, self.description, self.start, self.end)
            # pass

    def check_if_event_exists(self):
        if self.event_id in self.event_id_holder.event_ids:
            print("Looks like this event already exists. I won't create another one. You're welcome ")
            return True
