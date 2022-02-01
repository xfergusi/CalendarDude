import pytz

from AuthorizationSteve import AuthorizationSteve


class EventCreator:
    def makeAnEvent(self, summary, description, start, end, allday):
        time_period = "date"
        if(allday):
            time_period = "dataTime"
        service = AuthorizationSteve().get_service()
        event = {
            'summary': 'test',
            'description': 'A chance to hear more about Google\'s developer products.',
            'start': {
                'dateTime': '2022-01-28T09:00:00',
                time_period: 'Australia/Sydney',
            },
            'end': {
                'dateTime': '2022-01-28T17:00:00',
                time_period: 'Australia/Sydney',
            },
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
        print('Event created: %s' % (event.get('htmlLink')))

    def makeAnEvent(self, summary, description, start, end):
        self.makeAnEvent(summary, description, start, end, False)

    def makeAnAnAllDayEvent(self, summary, description, start, end):
        self.makeAnEvent(summary, description, start, end, True)
