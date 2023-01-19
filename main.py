import argparse

from AllisonVisits.AllisonVisitManager import AllisonVisitManager
from Learning import LearningManager
from Tides.TideLevelManager import TideLevelManager
from BackEnd.Testing2 import Testing2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--option', type=str, required=True)
    args = parser.parse_args()
    print('You are running: ', args.option)
    option = args.option
    if option == "allison":
        print("Running code for allison")
        AllisonVisitManager().generate_visits_on_gcal()
    if option == "test":
        print("Running code for test")
        Testing2().test()
    elif option == "tide" or option == "tides":
        print("Running code for low tide calendar importer")
        TideLevelManager().generate_tide_events()
    elif option == "learning":
        LearningManager.run()
    else:
        print("somehow you messed this up, try again")
        print("Here are your options, not case sensitive")
        print("allison : Runs that bit of code that creates events for allison")
        print("tide : pulls data to find low tides for the next bit")
        print("Quit : kills the program\n")






if __name__ == '__main__':
    main()
