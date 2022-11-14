import argparse
import json

parser = argparse.ArgumentParser(
    description=""
)

parser.add_argument("-f", "--file", help="File that wil be used as a template", type=str)
parser.add_argument("-l", "--file_language", help="Language of the choosen file", type=str)
parser.add_argument("-tr", "--translate", help="Language used to translate", type=str)

if __name__ == "__main__":
    args = parser.parse_args()
    with open(args.file, "r") as string_file:
        print(json.load(string_file))
