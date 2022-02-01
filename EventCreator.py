import pytz

from AuthorizationSteve import AuthorizationSteve


class EventCreator:
    def __make_an_event(self, summary, description, start, end, allday):
        time_period = "dateTime"
        if allday:
            time_period = "date"
        service = AuthorizationSteve().get_service()
        event = {
            'summary': summary,
            'description': description,
            'start': {
                time_period: str(start),
                'timeZone': 'Australia/Sydney',
            },
            'end': {
                time_period: str(end),
                'timeZone': 'Australia/Sydney',
            },
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
        print('Event created: %s' % (event.get('htmlLink')))

    def make_an_event(self, summary, description, start, end):
        self.__make_an_event(summary, description, start, end, False)

    def make_an_all_day_event(self, summary, description, start, end):
        self.__make_an_event(summary, description, start, end, True)
