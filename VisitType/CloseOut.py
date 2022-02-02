from Event import Event


class CloseOut:

    visit_status_effective = None

    def __init__(self, window_id, site_number, start):
        self.visit_status_effective = Event(window_id, site_number + " Visit Status Effective", start, start)

    def make_the_event(self):
        self.visit_status_effective.make_an_all_day_event()

    def check_if_events_already_exists(self):
        self.visit_status_effective.check_if_event_exists()