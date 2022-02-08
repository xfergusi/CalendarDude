from Event import Event


class InterimMonitoring:

    start_of_window = None
    end_of_window = None

    def __init__(self, site_number, start, end):
        self.start_of_window = Event(site_number + " Start of Window", start, start)
        self.end_of_window = Event(site_number + " End of Window", end, end)

    def make_the_events(self):
        self.start_of_window.make_an_all_day_event()
        self.end_of_window.make_an_all_day_event()
