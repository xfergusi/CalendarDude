import argparse

from AllisonVisits.AllisonVisitManager import AllisonVisitManager
from Bassam import BassamCodeManager
from Learning import LearningManager
from Tides.TideLevelManager import TideLevelManager


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--option', type=str, required=True)
    args = parser.parse_args()
    print('You are running: ', args.option)
    option = args.option
    if option == "allison":
        print("Running code for allison")
        AllisonVisitManager().generate_visits_on_gcal()
    elif option == "tide":
        print("Running code for low tide calendar importer")
        TideLevelManager().generate_tide_events()
    elif option == "bassam":
        print("running bassam code")
        BassamCodeManager.run()
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
