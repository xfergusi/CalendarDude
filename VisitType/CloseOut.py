from Event import Event
from IDCreator import IDCreator


class CloseOut:

    visit_status_effective = None

    def __init__(self, row_id, site_number, start):
        self.visit_status_effective = Event(IDCreator.create_id_for_allisons_visits(row_id, start),
                                            site_number + " Close out",
                                            start,
                                            start)

    def make_the_event(self):
        self.visit_status_effective.make_an_all_day_event()
