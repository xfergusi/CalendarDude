from Event import Event


class AlEvents():

    start_of_window = None
    end_of_window = None
    site_number = None

    def __init__(self, event_id, site_number, start, end):
        self.event_id = event_id
        self.site_number = site_number
        self.start = start
        self.end = end
        self.summary = self.site_number + " : "

    def makeTheEvents(self):


