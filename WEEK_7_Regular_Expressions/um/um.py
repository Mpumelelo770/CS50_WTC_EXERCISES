

import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):

    pattern = r"\bum\b"
    ums = re.findall(pattern, s, flags = re.IGNORECASE)
    return len(ums)




if __name__ == "__main__":
    main()
