from AuthorizationSteve import AuthorizationSteve
import pytz
from EventGrabber import EventGrabber
import requests
from bs4 import BeautifulSoup as bs

import pandas as pd


def main():
    data = pd.read_excel(r'als_data/Site-Visits-1.8-Site-Visit-Details.xlsx')
    print(data.get(0))


if __name__ == '__main__':
    main()
