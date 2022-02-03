import pytz

from AuthorizationSteve import AuthorizationSteve


class EventCreator:
    def __make_an_event(self, summary, description, start, end, allday):
        time_period = "dateTime"
        if allday:
            time_period = "date"
            start = start[0:10]
            end = end[0:10]
        event = {
            'summary': summary,
            'description': description,
            'start': {
                time_period: start,
                'timeZone': 'Australia/Sydney',
            },
            'end': {
                time_period: end,
                'timeZone': 'Australia/Sydney',
            },
        }

        # print(event)

        # service = AuthorizationSteve().get_service()
        # event = service.events().insert(calendarId='primary', body=event).execute()
        # print('Event created: %s' % (event.get('htmlLink')))

    def make_an_event(self, summary, description, start, end):
        self.__make_an_event(summary, description, start, end, False)

    def make_an_all_day_event(self, summary, description, start, end):
        self.__make_an_event(summary, description, start, end, True)
