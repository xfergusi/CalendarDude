import sys

from AllisonVisitManager import AllisonVisitManager
from TideLevelManager import TideLevelManager


def main():
    option = None
    while option != "quit":
        print("Here are your options, not case sensitive")
        print("Allison : Runs that bit of code that creates events for allison")
        print("tide : pulls data to find low tides for the next bit")
        print("Quit : kills the program\n")
        option = input("Whacha tryin' to do?\n").lower()
        # option = "allison"
        if option == "allison":
            print("Running code for allison")
            AllisonVisitManager().generate_visits_on_gcal()
            break
        elif option == "tide":
            print("Running code for low")
            TideLevelManager().generate_tide_events()
        elif option == quit:
            break
        else:
            print("somehow you messed this up, try again")


if __name__ == '__main__':
    main()
