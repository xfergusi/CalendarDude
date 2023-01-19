from ics import Calendar, Event

class Testing:
    def test(self):
        c = Calendar()
        e = Event()
        e.name = "My cool event"
        e.begin = '2023-01-19 00:00:00'
        c.events.add(e)
        c.events
        # [<Event 'My cool event' begin:2014-01-01 00:00:00 end:2014-01-01 00:00:01>]
        with open('my.ics', 'w') as my_file:
            my_file.writelines(c.serialize_iter())