import hashlib

from EventCreator import EventCreator
from EventGrabber import EventGrabber
from EventIDHolder import EventIDHolder


def set_id(summary, start, end):
    id_pre_hex = str(summary) + str(start) + str(end)
    id_pre_hex = id_pre_hex.encode('utf-8')
    print(id_pre_hex)
    return hashlib.sha256(id_pre_hex).hexdigest()


class Event:
    event_id = None
    summary = None
    description = None
    start = None
    end = None
    event_id_holder = None

    def __init__(self, summary, start, end):

        self.event_id = set_id(summary, start, end)
        self.summary = summary
        self.start = str(start)
        self.end = str(end)

    def make_an_all_day_event(self):
        if not self.check_if_event_exists():
            EventCreator().make_an_all_day_event(self.event_id, self.summary, self.description, self.start, self.end)

    def check_if_event_exists(self):
        if self.event_id in self.event_id_holder.event_ids:
            print("Looks like this event already exists. I won't create another one. You're welcome ")
            return True
