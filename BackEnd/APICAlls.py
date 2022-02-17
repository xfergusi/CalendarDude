from BackEnd.EventManager import EventManager

event_manager = EventManager()


def create_an_all_day_event(summary, start, end):
    event_manager.make_an_all_day_event(summary, start, end)


def create_an_event(summary, start, end):
    event_manager.make_an_event(summary, start, end)
