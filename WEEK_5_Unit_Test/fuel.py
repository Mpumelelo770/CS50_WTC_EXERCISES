

import sys

def main():
    value = input("Fraction: ")
    reading = convert(value)
    print(gauge(reading))






def convert(fraction):

    separate = fraction.split("/")
    numerator = int(separate[0])
    denominator = int(separate[1])
    gauge = numerator / denominator

    if numerator > denominator:
        raise ValueError()
    if numerator < 0 or denominator < 0:
        raise ValueError()

    percent = round(gauge * 100)
    return percent









def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"





if __name__ == "__main__":
    main()
