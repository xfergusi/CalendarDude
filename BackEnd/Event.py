
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
        self.end = str(end)

    # def make_an_all_day_event_direct_to_gcal(self):
    #     EventCreator().make_an_all_day_event_direct_to_gcal(self.event_id, self.summary, self.description, self.start, self.end)
    #
    # def make_an_event_direct_to_gcal(self):
    #     EventCreator().make_an_event_direct_to_gcal(        self.event_id, self.summary, self.description, self.start, self.end)

    # I think I should have an EventCreater, that takes in "Events" and poops out the ICS file
    # The brain can call the Event creater at the end of the program.