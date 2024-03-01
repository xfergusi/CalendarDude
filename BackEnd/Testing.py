# imports
from icalendar import Calendar, Event, vCalAddress, vText
from datetime import datetime, date
import hashlib
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
# from requests_html import HTMLSession


import os
import pytz

from BackEnd.APICAlls import create_an_all_day_event


class Testing:
    def test(self):

        tide_page = requests.get('https://www.ladbrokes.com.au/sports/baseball')
        tide_page = BeautifulSoup(tide_page.content, "html.parser")
        print(tide_page)

        # url = "https://www.ladbrokes.com.au/sports/baseball"
        # browser = webdriver.PhantomJS()
        # browser.get(url)
        # html = browser.page_source
        # soup = BeautifulSoup(html, "html.parser")
        # print(soup)
        # //a = soup.find('section', 'wrapper')
        # table = tide_page.find_all('div', {'class': 'class="sports-event-entry-with-markets"'})
        # print(table)
        # list_of_low_tide_datetimes = []
        # for row in table:
        #     low_tides = row.find_all('li', {'class': 'point-low'})
        #     for low_tide in low_tides:
        #         time_str = row.find("time").text + " " + low_tide.find("h3").text
        #
        # create_an_all_day_event("testing", datetime.now(), date(2023, 5, 6))
        # create_an_all_day_event("testing222", date(2023, 5, 6), date(2023, 5, 6))
