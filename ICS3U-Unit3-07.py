# Copyright (c) 2022 Evgeny Vovk All rights reserved.
#
# Created by: Evgeny Vovk
# Created on: October 2022
# ICS3U-Unit3-07.py File,
# learning and...or... statements in python.


def main():

    # input and variables
    age = input("Enter your age: ")

    # process and output
    print("")
    try:
        age = int(age)
        if age > 25 and age < 40:
            print("You are an acceptable age.")
        elif age <= 0 or age >= 120:
            print("Type in a valid age.")
        else:
            print("You are not an acceptable age.")
    except ValueError:
        print("Invalid input, Please try again following the requirements.")

    print("\n\nDone.")


if __name__ == "__main__":
    main()
