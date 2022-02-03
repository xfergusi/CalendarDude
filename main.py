import sys

from AllisonVisitManager import AllisonVisitManager


def main():
    option = None
    while option != "quit":
        print("Here are your options, not case sensitive")
        print("Allison : Runs that bit of code that creates events for allison")
        print("Quit : kills the program\n")
        # option = input("Whacha tryin' to do?\n").lower()
        option = "allison"
        if option == "allison":
            print("Running code for allison")
            AllisonVisitManager().generate_visits_on_gcal()
            break
        elif option == quit:
            break
        else:
            print("somehow you messed this up, try again")


if __name__ == '__main__':
    main()
