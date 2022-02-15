from datetime import datetime

import requests
from bs4 import BeautifulSoup

class WebScraper:
    def scrape_the_web_for_low_tides(self):
        tide_page = requests.get('https://tides.willyweather.com.au/nsw/sydney/bondi-beach.html')
        tide_page = BeautifulSoup(tide_page.text, "lxml")
        # print(tide_page)
        table = tide_page.find_all('li', {'class': 'day'})
        # print(f'Found {len(table)} table/tables.')
        list_of_low_tide_datetimes = []
        for row in table:
            # print("---------------")
            # print(row.find("time").text)
            low_tides = row.find_all('li', {'class': 'point-low'})
            # print(f'Found {len(low_tides)} table/tables.')
            # print(low_tides)
            for low_tide in low_tides:
                time_str = row.find("time").text + " " + low_tide.find("h3").text
                list_of_low_tide_datetimes.append(self.raw_string_to_datetime(time_str))
        return list_of_low_tide_datetimes

    def raw_string_to_datetime(self, string_to_convert):
        str_without_first_word = string_to_convert.split(' ', 1)[1] + " " + str(datetime.now().year)
        # print(str_without_first_word)
        return datetime.strptime(str_without_first_word, "%d %b %I:%M %p %Y")
        # print()

