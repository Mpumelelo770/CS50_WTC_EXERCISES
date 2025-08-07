


import inflect
p = inflect.engine()

def adu():
    try:
        names = []
        while True:
            name = input("Name: ")
            names.append(name)
    except EOFError:
        return f"Adieu, adieu, to {p.join(names)}"

print(adu())
