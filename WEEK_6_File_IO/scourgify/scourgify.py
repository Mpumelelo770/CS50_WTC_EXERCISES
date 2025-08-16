

import csv
import sys


def main():
    try:
        if len(sys.argv) != 3:
            raise IndexError()

    except IndexError:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")


    before = sys.argv[1]
    after = sys.argv[2]

    print(names(before, after))



def names(before, after):
    try:
        with open(before, "r") as original, open(after, "a") as edited:
            reader = csv.DictReader(original)
            writer = csv.DictWriter(edited, fieldnames = ["first","last","house"])
            writer.writeheader()

            for j in reader:
                first_name = j["name"].split(",")[1]
                last_name = j["name"].split(",")[0]
                location = j["house"]
                writer.writerow({"first": first_name, "last": last_name, "house":location})
    except FileNotFoundError:
        sys.exit(f"Could not read {before}")






if __name__ == "__main__":
    main()


