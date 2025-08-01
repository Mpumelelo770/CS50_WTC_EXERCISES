

def date():

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    result = ""
    while True:
        n = input("Date: ").strip()
        try:
            if n == "A":
                return n
            elif n[0].isdigit():

                list = n.split("/")
                new_list = [int(i) for i in list]
                if new_list[0] > 12 or new_list[1] > 31:
                    raise Exception()
                result += str(new_list[2])
                result += "-"
                result += str(f"{new_list[0]:02}")
                result += "-"
                result += str(f"{new_list[1]:02}")
                return result
            else:

                list = n.split()
                list[1] = list[1][0]
                if months.index(list[0]) + 1 > 12 or int(list[1]) > 31:
                    break
                    #raise Exception()
                result += list[2]
                result += "-"
                result += str(f"{months.index(list[0]) + 1:02}")
                result += "-"
                result += str(f"{int(list[1]):02}")
                return result
        except:
            print("Invalid input")




print(date())




