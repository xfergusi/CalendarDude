from datetime import timedelta

from BackEnd.Event import Event
from Tides.WebScraper import WebScraper


class TideLevelManager:

    def generate_tide_events(self):
        list_of_low_time_events = WebScraper().scrape_the_web_for_low_tides()
        for low_tide in list_of_low_time_events:
            Event("low tide point",
                  (low_tide - timedelta(hours=1)).isoformat(),
                  (low_tide + timedelta(hours=1)).isoformat()
                  ).make_an_event()


