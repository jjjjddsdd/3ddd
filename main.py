import sys
from PIL import Image


def main() -> None:
    # open file
    try:
        file = open(sys.argv[1], "r")
        print(file)
    except FileNotFoundError:
        print("File does not exist.")


main()
