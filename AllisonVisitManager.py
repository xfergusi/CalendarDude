
import pandas as pd

from VisitType.InterimMonitoring import InterimMonitoring
from VisitType.CloseOut import CloseOut


class AllisonVisitManager:
    def generate_visits_on_gcal(self):
        data = pd.read_excel(r'als_data/Site-Visits-1.8-Site-Visit-Details.xlsx')

        only_planned_df = data.loc[data['Visit Status'] == 'Planned']
        for index, row in only_planned_df.iterrows():
            # if pd.isnull(row["Visit Window Min Date"]):
            #     continue
            # if row['Site Visit Row ID'] != "1-ZQUABI8":
            #     continue
            if row["Visit Type"] == "Interim Monitoring":
                interim = InterimMonitoring(row["Site Visit Row ID"],
                                             row["Site #"],
                                             row["Visit Window Min Date"],
                                             row['Visit Window Max Date'])
                # print(row["Site #"], row["Visit Window Min Date"], row["Visit Window Max Date"], row['Site Visit Row ID'])
                interim.make_the_events()
            elif row["Visit Type"] == "Close-Out":
                closing = CloseOut(row["Site Visit Row ID"],
                                             row["Site #"],
                                             row['Visit Status Effective'])
                closing.make_the_event()
