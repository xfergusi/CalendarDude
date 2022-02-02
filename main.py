import sys


def main():
    option = None
    while option != "quit":
        option = input("Whacha tryin' to do?").lower()
        if option == 'Allison':
            # Select random nice phrase
            print("Running code for allison")
            # AllisonVisitManager().generate_visits_on_gcal()
        elif option == quit:
            break
        else:
            print("Here are your options, not case sensitive")
            print("Allison : Runs that bit of code that creates events for allison")
            print("Quit : kills the program\n")


if __name__ == '__main__':
    main()
