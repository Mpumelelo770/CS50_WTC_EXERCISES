

from tabulate import tabulate
import csv
import sys



def main():
    try:
        if len(sys.argv) != 2:
            raise IndexError()
        if sys.argv[1][-3:] != "csv":
            raise Exception()


    except IndexError:
        sys.exit("Invalid command-line arguments")
    except Exception:
        sys.exit("Not a csv file")


    name = sys.argv[1]
    print(table(name))




def table(data):
    try:
        with open(data, "r") as file:
            reader = csv.reader(file)
            return tabulate(reader, headers = "firstrow",tablefmt = "grid")
    except FileNotFoundError:
        sys.exit("File does not exist")


main()
