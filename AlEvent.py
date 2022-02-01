from Event import Event


class AlEvent(Event):

    site_number = None

    def __init__(self, event_id, site_number, start, end):
        self.event_id = event_id
        self.site_number = site_number
        self.start = start
        self.end = end
