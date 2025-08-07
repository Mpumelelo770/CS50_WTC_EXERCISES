

import random

def main():
    n = get_level()
    z = generate_integer(n)
    print(z)



def get_level():

    levels = [1, 2, 3]

    while True:
        try:
            level = int(input("Please enter a level: "))
            if level not in levels:
                continue
            return level

        except ValueError:
            continue




def generate_integer(n):

    if n == 1:
        a, b = 0, 9
    elif n == 2:
        a, b = 10, 99

    elif n == 3:
        a, b = 100, 999

    score = 0
    for _ in range(10):
        count = 0
        x = random.randint(a, b)
        y = random.randint(a, b)
        compute = input(f"{x} + {y} = ").strip()



        if str(x + y) == compute:
            score += 1
        elif str(x + y) != compute:
            print("EEE")
            count = 1

            for i in range(2):
                compute = input(f"{x} + {y} = ").strip()
                if str(x + y) == compute:
                    score += 1
                    break

                elif str(x + y) != compute:
                    print("EEE")
                    count += 1

            if count == 3:
                print(f"{x} + {y} = {x + y}")





    return score






if __name__ == "__main__":
    main()

