import pandas as pd

from BackEnd.APICAlls import create_an_event
from datetime import datetime

class AllisonVisitManager:
    def generate_visits_on_gcal(self):
        data = pd.read_excel(r'AllisonVisits/als_data/sites02052023.xlsx')
        only_planned_df = data.loc[data['Visit Status'] == 'Planned']
        for index, row in only_planned_df.iterrows():
            if row["Visit Type"] == "Interim Monitoring" and row["Visit Window Max Date"].strftime("%Y %m") == "2023 05":
                self.make_interim_monitoring_events(row["Site #"],
                                                    row["Visit Window Min Date"],
                                                    row['Visit Window Max Date'])
            elif row["Visit Type"] == "Close-Out" and row["Visit Status Effective Date"].strftime("%Y") == "2023":
                self.make_close_out_event(row["Site #"],
                                          row['Visit Status Effective Date'])

    def make_interim_monitoring_events(self, site_number, start, end):
        start = datetime.strptime(str(start), '%Y-%m-%d %H:%M:%S').date()
        end = datetime.strptime(str(end), '%Y-%m-%d %H:%M:%S').date()
        create_an_event(str(site_number) + " Start of Window", start, start)
        create_an_event(str(site_number) + " End of Window", end, end)

    def make_close_out_event(self, site_number, start):
        start = datetime.strptime(str(start), '%Y-%m-%d %H:%M:%S').date()
        create_an_event(str(site_number) + " Close out", start, start)
