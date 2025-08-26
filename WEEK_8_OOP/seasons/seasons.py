
from datetime import date
import sys
import inflect



def main():
    dob = input("Date of birth: ")
    
    try:
        print(get_minutes(dob))
    except ValueError:
        sys.exit("Invalid input")






def get_minutes(dob):


    date.fromisoformat(dob) #error if dob format not YYYY-MM-DD


    year, month, day = dob.split("-")

    current_date = date.today()
    d = date(int(year), int(month), int(day))  #new object of the date class


    diff = current_date - d   #operator overloading (__sub__) in date class

    #converts numerals to words
    p = inflect.engine()
    words = p.number_to_words(diff.days * 24 * 60)

    #removes "and" in the string
    separate = words.split(" ")
    new = [x for x in separate if x != "and"]
    final = " ".join(new)

    return f"{final.capitalize()} minutes"



if __name__ == "__main__":
    main()
