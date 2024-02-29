import pandas as pd

from BackEnd.APICAlls import create_an_event
from datetime import datetime


def make_close_out_event(site_number, start):
    start = datetime.strptime(str(start), '%Y-%m-%d %H:%M:%S').date()
    create_an_event(str(site_number) + " Close out", start, start)


def strdate_to_date(str_date):
    return datetime.strptime(str(str_date), '%Y-%m-%d %H:%M:%S').date()


def make_interim_monitoring_events(site_number, start, end):
    start = strdate_to_date(start)
    end = strdate_to_date(end)
    create_an_event(str(site_number) + " Start of Window", start, start)
    create_an_event(str(site_number) + " End of Window", end, end)


def generate_visits_on_gcal():
    data = pd.read_excel(r'AllisonVisits/ForFergz.xlsx')
    only_planned_df = data.loc[data['Monitoring Event Status'] == 'Planned']
    for index, row in only_planned_df.iterrows():
        if pd.isnull(row["Monitoring Event Window Max Date (Siebel)"]):
            continue
        # if row["Monitoring Event Type"] == "Monitoring Event" and row["Monitoring Event Window Max Date (Siebel)"].strftime("%Y") == "2024":
        if row["Monitoring Event Type"] == "Monitoring Event":
            make_interim_monitoring_events(row["Site #"],
                                                row["Monitoring Event Window Min Date (Siebel)"],
                                                row["Monitoring Event Window Max Date (Siebel)"])
        # elif row["Monitoring Event Type"] == "Close-Out Event" and row["Monitoring Event Status Effective Date"].strftime("%Y") == "2024":
        #     make_close_out_event(row["Site #"],
        #                               row['Monitoring Event Status Effective Date'])
