
class Event:
    event_id = None
    summary = None
    description = ""
    start = None
    end = None

    def __init__(self, event_id, summary, start, end):
        self.event_id = event_id
        self.summary = summary
        self.start = start
        self.end = end
