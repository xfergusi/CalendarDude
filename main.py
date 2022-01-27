from AuthorizationSteve import AuthorizationSteve
import pytz
from EventGrabber import EventGrabber


def main():
    print(pytz.all_timezones)
    service = AuthorizationSteve().get_service()
    event = {
        'summary': 'test',
        'description': 'A chance to hear more about Google\'s developer products.',
        'start': {
            'dateTime': '2022-01-28T09:00:00',
            'timeZone': 'Australia/Sydney',
        },
        'end': {
            'dateTime': '2022-01-28T17:00:00',
            'timeZone': 'Australia/Sydney',
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))


if __name__ == '__main__':
    main()
