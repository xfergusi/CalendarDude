import datetime
from datetime import timedelta

from BackEnd.APICAlls import create_an_event
from Tides.WebScraper import scrape_the_web_for_low_tides, scrape_the_web_for_sunrise_and_set


def generate_tide_events():
    list_of_low_time_events = scrape_the_web_for_low_tides()
    list_of_rise_and_set = scrape_the_web_for_sunrise_and_set()
    print(list_of_rise_and_set)
    print(datetime.time(int(list_of_rise_and_set[1].split(":")[0])+1))
    for low_tide in list_of_low_time_events:
        if datetime.time(int(list_of_rise_and_set[0].split(":")[0])) < \
                low_tide.time() < \
                datetime.time(int(list_of_rise_and_set[1].split(":")[0])+1):
            create_an_event("low tide point",
                            (low_tide - timedelta(hours=1)),
                            (low_tide + timedelta(hours=1))
                            )
        else:
            print("This tide is out of the time range, we don't make it: " + str(low_tide))
