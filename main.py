from AlEvent import AlEvent
from AuthorizationSteve import AuthorizationSteve
import pytz

from Event import Event
from EventGrabber import EventGrabber
import requests
from bs4 import BeautifulSoup as bs

import pandas as pd


def main():
    data = pd.read_excel(r'als_data/Site-Visits-1.8-Site-Visit-Details.xlsx')

    only_planned_df = data.loc[data['Visit Status'] == 'Planned']
    for index, row in only_planned_df.iterrows():
        print(row["Site #"], row["Visit Window Min Date"], row["Visit Window Max Date"], row['Site Visit Row ID'])
        al_event = AlEvent(row["Site Visit Row ID"],
                           row["Site #"],
                           row["Visit Window Min Date"],
                           row['Visit Window Min Date'])
        al_event.makeTheEvents()
        print(al_event)




if __name__ == '__main__':
    main()
