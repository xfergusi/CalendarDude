import datetime
from datetime import timedelta

from BackEnd.APICAlls import create_an_event
from Tides.WebScraper import WebScraper


class TideLevelManager:

    def generate_tide_events(self):
        list_of_low_time_events = WebScraper().scrape_the_web_for_low_tides()
        for low_tide in list_of_low_time_events:
            if datetime.time(5, 30) < low_tide.time() < datetime.time(22, 00):
                create_an_event("low tide point",
                                (low_tide - timedelta(hours=1)).isoformat(),
                                (low_tide + timedelta(hours=1)).isoformat()
                                )
            else:
                print("This tide is out of the time range, we don't make it: " + str(low_tide))