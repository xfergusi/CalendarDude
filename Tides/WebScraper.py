from datetime import datetime

import requests
from bs4 import BeautifulSoup


def raw_string_to_datetime(string_to_convert):
    str_without_first_word = string_to_convert.split(' ', 1)[1] + " " + str(datetime.now().year)
    print(str_without_first_word)
    return datetime.strptime(str_without_first_word, "%d %b %I:%M %p %Y")


def scrape_the_web_for_low_tides():
    tide_page = requests.get('https://tides.willyweather.com.au/nsw/sydney/bondi-beach.html')
    tide_page = BeautifulSoup(tide_page.text, "lxml")
    table = tide_page.find_all('li', {'class': 'day'})
    list_of_low_tide_datetimes = []
    for row in table:
        low_tides = row.find_all('li', {'class': 'point-low'})
        for low_tide in low_tides:
            time_str = row.find("time").text + " " + low_tide.find("h3").text
            list_of_low_tide_datetimes.append(raw_string_to_datetime(time_str))
    return list_of_low_tide_datetimes
