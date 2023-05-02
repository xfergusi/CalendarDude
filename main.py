import argparse

from AllisonVisits.AllisonVisitManager import AllisonVisitManager
from InputParams import InputParams
from Learning import LearningManager
from Tides.TideLevelManager import TideLevelManager
from BackEnd.Testing2 import Testing2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--program', type=str, required=True)
    parser.add_argument('--input_method', type=str, required=True)
    args = parser.parse_args()
    print('You are running -%s- program ', args.option)
    print('You are running -%s- input method ', args.input_method)
    input_params = InputParams(args.option, args.input_method)
    if input_params.program == "allison":
        print("Running code for allison")
        AllisonVisitManager().generate_visits_on_gcal(input_params)
    if input_params.program == "test":
        print("Running code for test")
        Testing2().test()
    elif input_params.program == "tide" or input_params.program == "tides":
        print("Running code for low tide calendar importer")
        TideLevelManager().generate_tide_events()
    elif input_params.program == "learning":
        LearningManager.run()
    else:
        print("somehow you messed this up, try again")
        print("Here are your options, not case sensitive")
        print("allison : Runs that bit of code that creates events for allison")
        print("tide : pulls data to find low tides for the next bit")
        print("Quit : kills the program\n")






if __name__ == '__main__':
    main()
