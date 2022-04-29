#!/usr/bin/env python3
# Created by: Hunter Connolly
# Created on: April 28, 2022
# This program asks the user for the number of numbers to add together.
# It then uses a while loop to ask the user for the number to add
# and If it is a whole number, add it to the current sum. Otherwise,
# don't and continue the loop then display the numbers added and the final sum


def main():
    # Get the user input as a string
    user_input_string = input("How many numbers would you like added?: ")
    print("")

    try:
        # cast the user number to int
        user_input = int(user_input_string)

        if user_input < 0:
            print("Your number cannot be negative!")
        else:
            # initialize sum equation, sum and counter
            sum_equation = ""
            sum = 0
            counter = 0

            # get the numbers the user would like added
            while True:
                user_num_string = input("What number would you like added?: ")
                try:
                    user_num = int(user_num_string)
                    if user_num > 0:
                        counter = counter + 1
                        print("{0} added to total".format(user_num))
                        sum += user_num
                    # if the number is less than 0 then it will not be added
                    else:
                        print("Number cannot be <= 0 so it was not added!")
                        continue
                # if number is invalid then do not add it to total
                except Exception:
                    print("Number has to be a whole number, so it was not added to the total")
                    continue
                if counter >= user_input:
                    print("sum = {}".format(sum))
                    break

    except Exception:
        print("That is not a number!! Try Again!")
        print("")


if __name__ == "__main__":
    main()
