

import re
import sys


def main():
     print(parse(input("HTML: ")))




def parse(s):
     pattern = r'"https?://(?:www\.)?youtube\.com/embed/(xvFZjo5PgG0)".*(iframe>)$'
     matches = re.search(pattern,s)

     if matches:
          identifyer = matches.group(1)
          return f"https://youtu.be/{identifyer}"
     else:
          return None




if __name__ == "__main__":
     main()
