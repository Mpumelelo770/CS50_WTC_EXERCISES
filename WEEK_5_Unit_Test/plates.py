

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")





def is_valid(s):
    count = 0

    if len(s) > 6 or len(s) < 2:
        return False

    else:
        for letter in s:
            if letter.isalpha():
                count += 1
            else:
                break

        if count == len(s):  #all letters
            return True

        left = s[count:]

        if left[0] == "0":
            return False
        elif count < 2:
            return False  #first 2 inouts not letters
        else:
            for j in left:
                if not j.isdigit():
                    return False

    return True





if __name__ == "__main__":
    main()



