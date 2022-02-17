from datetime import datetime

from BackEnd.APICAlls import create_an_event, create_an_all_day_event


def run():
    create_an_all_day_event("test event", datetime.now().isoformat(), datetime.now().isoformat())
