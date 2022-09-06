#!/usr/bin/env python
"""
Author: Scott Schmidl
Date: 09/06/2022
"""

import argparse
from va_dis_rating import DisabilityRatingCalculator

def run(args):
    # match the "dest": dest="input", if a flag instead of position argument is given
    ratings = args.input
    return ratings

def main():
    parser = argparse.ArgumentParser(description="Calculate disability percent")

    # NOTE: other arguments are dest and required if using a flag(a value proceeded by, "-") instead of position argument
    parser.add_argument("input",
                        nargs="+",
                        type=int,
                        choices=range(10, 101, 10),
                        help="""list of ratings used to calculate percentage.
                                Of the form: numA, numB, numC""", )

    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)

    drc = DisabilityRatingCalculator()
    final_rating = drc.calculate(run(args))
    print(f"Your final disability rating is: {final_rating}%")

if __name__ == "__main__":
    main()