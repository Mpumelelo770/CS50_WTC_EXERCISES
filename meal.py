def main():
    t = input("Time:")
    converted = convert(t)
    if 7.00 <= converted <= 8.00:
        print("Breakfast time")
    elif 12.00 <= converted <= 13.00:
        print("Lunch time")
    elif 18.00 <= converted <= 19.00:
        print("Dinner time")


def convert(time):
    hours, minutes = time.split(":")
    minutes = float(minutes)/60
    correct = float(hours) + minutes
    return correct


if __name__ == "__main__":
    main()