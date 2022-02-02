from EventCreator import EventCreator
from EventGrabber import EventGrabber


class Event:
    event_id = None
    summary = None
    description = None
    start = None
    end = None

    def __init__(self, event_id, summary, start, end):
        self.event_id = event_id
        self.summary = summary
        self.description = event_id
        self.start = str(start)
        self.end = str(end)

    def make_an_all_day_event(self):
        EventCreator().make_an_all_day_event(self.summary, self.description, self.start, self.end)

    def check_if_event_exists(self):
        pass
        # EventGrabber.get_events_by_date_range()

