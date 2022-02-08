from Event import Event


class CloseOut:

    visit_status_effective = None

    def __init__(self, site_number, start):
        self.visit_status_effective = Event(site_number + " Close out", start, start)

    def make_the_event(self):
        self.visit_status_effective.make_an_all_day_event()
