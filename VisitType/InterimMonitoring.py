from IDCreator import IDCreator
from Event import Event


class InterimMonitoring:

    start_of_window = None
    end_of_window = None

    def __init__(self, row_id, site_number, start, end):
        self.start_of_window = Event(IDCreator.create_id_for_allisons_visits(row_id, start),
                                     site_number + " Start of Window",
                                     start,
                                     start)
        self.end_of_window = Event(IDCreator.create_id_for_allisons_visits(row_id, end),
                                   site_number + " End of Window",
                                   end,
                                   end)

    def make_the_events(self):
        self.start_of_window.make_an_all_day_event()
        self.end_of_window.make_an_all_day_event()
