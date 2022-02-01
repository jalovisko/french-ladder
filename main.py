import argparse
import sys

from num2words import num2words

def main():
    parser = argparse.ArgumentParser(
        description = 'This program generates a French word for an integer number of user choise')
    parser.add_argument('number',
            metavar = 'number',
            type = int,
            help = 'an integer number')
    args, _ = parser.parse_known_args()
    if args.number is None:
        sys.stderr.write('error: a number was not specified')
        parser.print_help()
        sys.exit(2)
    print(num2words(args.number, lang = 'fr'))
    sys.exit(0)

if __name__ == '__main__':
    main()
