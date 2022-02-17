from datetime import timedelta

from BackEnd.APICAlls import create_an_event
from Tides.WebScraper import WebScraper


class TideLevelManager:

    def generate_tide_events(self):
        list_of_low_time_events = WebScraper().scrape_the_web_for_low_tides()
        for low_tide in list_of_low_time_events:
            create_an_event("low tide point",
                            (low_tide - timedelta(hours=1)).isoformat(),
                            (low_tide + timedelta(hours=1)).isoformat()
                            )
