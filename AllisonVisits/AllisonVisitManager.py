import pandas as pd

from BackEnd.APICAlls import create_an_all_day_event


class AllisonVisitManager:
    def generate_visits_on_gcal(self, input_params):
        data = pd.read_excel(r'AllisonVisits/als_data/Allison_Site_Visits.xlsx')
        only_planned_df = data.loc[data['Visit Status'] == 'Planned']
        for index, row in only_planned_df.iterrows():
            if row["Visit Type"] == "Interim Monitoring":
                self.make_interim_monitoring_events(row["Site #"],
                                                    row["Visit Window Min Date"],
                                                    row['Visit Window Max Date'])
            elif row["Visit Type"] == "Close-Out":
                self.make_close_out_event(row["Site #"],
                                          row['Visit Status Effective'])

    def make_interim_monitoring_events(self, site_number, start, end):
        create_an_all_day_event(site_number + " Start of Window", start, start)
        create_an_all_day_event(site_number + " End of Window", end, end)

    def make_close_out_event(self, site_number, start):
        create_an_all_day_event(site_number + " Close out", start, start)
