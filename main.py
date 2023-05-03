import argparse

from AllisonVisits.AllisonVisitManager import AllisonVisitManager
from BackEnd.TheBrain import TheBrain
from InputParams import InputParams
from Learning import LearningManager
from Tides.TideLevelManager import TideLevelManager
from BackEnd.Testing2 import Testing2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--program', type=str, required=True)
    args = parser.parse_args()
    print('You are running -%s- program ', args.program)
    if args.program == "allison":
        print("Running code for allison")
        AllisonVisitManager().generate_visits_on_gcal()
    if args.program == "test":
        print("Running code for test")
        Testing2().test()
    elif args.program == "tide" or args.program == "tides":
        print("Running code for low tide calendar importer")
        TideLevelManager().generate_tide_events()
    elif args.program == "learning":
        LearningManager.run()
    else:
        print("somehow you messed this up, try again")
        print("Here are your options, not case sensitive")
        print("allison : Runs that bit of code that creates events for allison")
        print("tide : pulls data to find low tides for the next bit")
        print("Quit : kills the program\n")

    the_brain = TheBrain()
    print(len(the_brain.list_of_events))
    the_brain.create_the_events()




if __name__ == '__main__':
    main()
