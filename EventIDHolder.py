from EventGrabber import EventGrabber


class EventIDHolder:
    event_ids = []

    def __init__(self):
        self.event_ids = EventGrabber().get_all_event_ids_after_now()
