import argparse

from AllisonVisits.AllisonVisitManager import generate_visits_on_gcal
from BackEnd.EventManager import EventManager
from Learning import LearningManager
from Tides.TideLevelManager import generate_tide_events
from BackEnd.Testing import Testing


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--program', type=str, required=True)
    args = parser.parse_args()
    print(f'You are running {args.program} program')
    if args.program == "allison":
        print("Running code for allison")
        generate_visits_on_gcal()
    if args.program == "test":
        print("Running code for test")
        Testing().test()
    elif args.program == "tide" or args.program == "tides":
        print("Running code for low tide calendar importer")
        generate_tide_events()
    elif args.program == "how-to":
        LearningManager.run()
    else:
        print("somehow you messed this up, try again")
        print("Here are your options, not case sensitive")
        print("allison : Runs that bit of code that creates events for allison")
        print("tide : pulls data to find low tides for the next bit")
        print("Quit : kills the program\n")

    EventManager().make_the_ics_file()


if __name__ == '__main__':
    main()
