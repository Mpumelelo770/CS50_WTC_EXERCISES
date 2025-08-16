

#A function that greets the user
""" This is a docstring
that should be counted as part of
the comments but the program

should take it into consideration"""


def main():
    name = input("Name: ")
    print(greet(name))


def greet(name):
    return f"Hello, {name}"

main()

