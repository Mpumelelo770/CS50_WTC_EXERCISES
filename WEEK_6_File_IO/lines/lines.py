


import sys

def main():
    try:
        if len(sys.argv) != 2:
            raise IndexError()
    except IndexError:
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")

    try:
        if sys.argv[1][-2:] != "py":
           raise Exception()
    except Exception:
        sys.exit("Not a python file")

    name = sys.argv[1]
    print(lines(name))





def lines(document):
    try:
        with open(document,"r") as file:
            reader = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    count = 0

    for i in reader:
        if i.strip().startswith("#") or i.strip() == "":
            continue
        count += 1

    return count




if __name__ == "__main__":
    main()








