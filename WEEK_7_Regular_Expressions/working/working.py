

import re
import sys


def main():
    time = validate_convert(convert, input("Hours: "))

    print(time)




def validate_convert(func, s):
    pattern = r"^(?P<start_hours>[1-9]|1[0-2]):?(?P<start_minutes>[0-5][0-9])? (?P<start_ind>AM|PM) to (?P<end_hours>[1-9]|1[0-2]):?(?P<end_minutes>[0-5][0-9])? (?P<end_ind>AM|PM)$"

    matches = re.match(pattern, s)

    if matches:
        start_hour = matches.group("start_hours")
        start_minute = matches.group("start_minutes")
        start_i = matches.group("start_ind")
        end_hour = matches.group("end_hours")
        end_minute = matches.group("end_minutes")
        end_i = matches.group("end_ind")

        return f"{func(start_hour, start_minute, start_i)} to {func(end_hour, end_minute, end_i)}"
    else:
        raise ValueError()




def convert(hour,minute,i):

    if minute == None:
        if i == "AM":
            if hour == "12":
                return f"{int(hour) - 12:02}:00"
            elif hour != "12":
                return f"{int(hour):02}:00"

        elif i == "PM":
            if hour != "12":
                return f"{int(hour) + 12:02}:00"
            elif hour == "12":
                return f"{int(hour):02}:00"


    elif minute != None:
        if i == "AM":
            if hour == "12":
                return f"{int(hour) - 12:02}:{minute}"
            elif hour != 12:
                return f"{int(hour):02}:{minute}"
        elif i == "PM":
            if hour != "12":
                return f"{int(hour) + 12:02}:{minute}"
            elif hour == "12":
                return f"{int(hour):02}:{minute}"



if __name__ == "__main__":
    main()
