import argparse
import sys
from birthdays_package import birthdays

def parse_arguments(currencies, companies):
    parser = argparse.ArgumentParser(
            description="Get name of someone you want to know the birthday of",
            prog="birthdays")
    parser.add_argument("name",
                        help='''The name of the person you want to know
                        the birthday of.''')
    parser.add_argument("--version", action="version", version="1.0")
    args = parser.parse_args()
    return args
    
# if the user correctly provides a person name
if len(sys.argv) > 1:
    name = sys.argv[1]
    birthday = birthdays.return_birthday(name)
    # if the person is not found in the dictionary
    if not birthday:
        print("Sorry, we don't have {}'s birthday".format(name))
    else:
        print("{}' birthday is: {}".format(name, birthday))

else:
    print("Please tell me the person you want to know the birthday of.")
    exit()
