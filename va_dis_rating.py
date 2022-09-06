"""
Program to calculate the percent disability rating of a veteran
Author: Scott Schmidl
Date: 09/06/2022
"""

class DisabilityRatingCalculator:

    def calculate(self, ratings):
        while True:
            correct = input("Please verify ratings are correct, enter: y or n: ").lower()

            if correct not in ["y", "yes"]:
                print("Oops, try again")
                ratings = input("Please enter your ratings separated by spaces: ")
                ratings = [int(rating) for rating in ratings.split()]

            else: break

        if max(ratings) == 100:
            return 100

        else:
            total_body = 100
            percentage = 0

            while (total_body > 0) or (percentage <= 100):
                if not ratings:
                    return round(percentage, -1)

                else:
                    max_rating = ratings.pop(ratings.index(max(ratings)))
                    running = round(total_body * (max_rating / 100))
                    percentage += running
                    total_body -= running
