import argparse

from AllisonVisits.AllisonVisitManager import generate_visits_on_gcal
from BackEnd.EventManager import EventManager
from Learning import LearningManager
from Tides.TideLevelManager import generate_tide_events
from BackEnd.Testing import Testing


def main():
    program = arg_setup()

    if program == "allison":
        print("Running code for allison")
        generate_visits_on_gcal()
    elif program == "test":
        print("Running code for test")
        Testing().test()
    elif program == "tide" or program == "tides":
        print("Running code for low tide calendar importer")
        generate_tide_events()
    elif program == "how-to":
        LearningManager.run()
    else:
        print("\nSomehow you messed this up, try again")
        print("Here are your options, not case sensitive")
        print("allison : Runs that bit of code that creates events for allison")
        print("tide : pulls data to find low tides for the next bit")

    EventManager().make_the_ics_file()


def arg_setup():
    parser = argparse.ArgumentParser()
    parser.add_argument('--program', type=str, required=True)
    args = parser.parse_args()
    program = args.program.lower()
    print(f'You are running "{program}" program')
    return program


if __name__ == '__main__':
    main()
