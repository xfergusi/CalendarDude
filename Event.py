from EventCreator import EventCreator


class Event:
    event_id = None
    summary = None
    description = None
    start = None
    end = None

    def __init__(self, event_id, summary, description, start, end):
        self.event_id = event_id
        self.summary = summary
        self.description = description
        self.start = start
        self.end = end

    def createGCalEvent(self):
        EventCreator().makeAnEvent(self.summary, self.description, self.start, self.end)
