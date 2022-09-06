"""
Program to calculate the percent disability rating of a veteran
Author: Scott Schmidl
Date: 09/06/2022
"""

class DisabilityRatingCalculator:

    def calculate(self, ratings):
        print(ratings)

        if max(ratings) == 100:
            return 100

        else:
            total_body = 100
            percentage = 0
            if not ratings:
                return percentage

            else:
                max_rating = ratings.pop(ratings.index(max(ratings)))
                percentage += total_body * (max_rating / 100)
                total_body -= max_rating

        return percentage