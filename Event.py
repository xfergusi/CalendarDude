from EventCreator import EventCreator


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
        self.start = start
        self.end = end

    def make_an_all_day_event(self):
        EventCreator().make_an_all_day_event(self.summary, self.description, self.start, self.end)
