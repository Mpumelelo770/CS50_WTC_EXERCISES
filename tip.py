def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    remove_dollar = float(d[1:])
    return remove_dollar


def percent_to_float(p):
    remove_percent = float(p[:-1])
    return remove_percent/100



main()