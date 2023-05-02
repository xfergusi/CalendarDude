from BackEnd.EventCreator import EventCreator


class TheBrain:

    list_of_events = []

    def create_the_events(self):
        EventCreator.make_an_event(self, self.list_of_events)
    # every time the api is called, they tell the brain to remember it so it can do the work at the end