#!/usr/bin/env python

"""
Program to calculate the percent disability rating of a veteran
"""

import argparse

class DisabilityRatingCalculator:

    def calculate():
        pass


def run(args):

    # match the "dest": dest="input", if a flag instead of positional argument is given
    ratings = args.input
    print(ratings)

def main():
	parser = argparse.ArgumentParser(description="Calculator disability percent")

	# NOTE: other arguments are dest and required if using a flag(a value proceed by a -) instead of position argument
	parser.add_argument("ratings",
                     	help="""list of ratings used to calculate percentage.
                                Of the form: numA numB numC""",
                      	type=str,)

	parser.set_defaults(func=run)
	args = parser.parse_args()
	args.func(args)

    print(DisabilityRatingCalculator().calculate())

if __name__ == "__main__":
    main()