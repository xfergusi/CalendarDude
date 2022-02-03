from EventCreator import EventCreator
from EventGrabber import EventGrabber
from EventIDHolder import EventIDHolder


class Event:
    event_id = None
    summary = None
    description = None
    start = None
    end = None
    event_id_holder = None

    def __init__(self, event_id, summary, start, end):
        self.event_id = event_id
        self.summary = summary
        self.description = event_id
        self.start = str(start)
        self.end = str(end)
        self.event_id_holder = EventIDHolder()

    def make_an_all_day_event(self):
        if not self.check_if_event_exists():
            EventCreator().make_an_all_day_event(self.event_id, self.summary, self.description, self.start, self.end)

    def check_if_event_exists(self):
        if self.event_id in self.event_id_holder.event_ids:
            print("Looks like this event already exists. I won't create another one. You're welcome ")
            return True


