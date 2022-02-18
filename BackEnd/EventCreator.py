from googleapiclient.errors import HttpError

from BackEnd.AuthorizationSteve import AuthorizationSteve


class EventCreator:
    def __make_an_event(self, event_id, summary, description, start, end, allday):
        time_period = "dateTime"
        if allday:
            time_period = "date"
            start = start[0:10]
            end = end[0:10]
        event = {
            'summary': summary,
            'description': description,
            'id': event_id,
            'start': {
                time_period: start,
                'timeZone': 'Australia/Sydney',
            },
            'end': {
                time_period: end,
                'timeZone': 'Australia/Sydney',
            },
        }

        service = AuthorizationSteve().get_service()
        try:
            event = service.events().insert(calendarId='primary', body=event).execute()
            print('Event created: %s' % (event.get('htmlLink')))
        except HttpError as error:
            if error.status_code == 409:
                print(error.reason + " This should be ok. I probably deleted something: " + start)
                pass


    def make_an_event(self, event_id, summary, description, start, end):
        self.__make_an_event(event_id, summary, description, start, end, False)

    def make_an_all_day_event(self, event_id, summary, description, start, end):
        self.__make_an_event(event_id, summary, description, start, end, True)
