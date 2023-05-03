from BackEnd.EventCreator import EventCreator


class TheBrain:

    list_of_events = []

    def create_the_events(self):
        EventCreator.make_an_event(self, self.list_of_events)