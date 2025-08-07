import random


def main():
    n = level()
    m = play(n)
    print(m)



#Function for getting level and printing nums up to level

def level():
    while True:
        try:
            level = int(input("Enter a level: "))
            if level < 1:
                continue
        except ValueError:
            continue

        return list(range(1, level + 1))


#get random number between 1 and level for user to guess

def play(numbers):
    correct = random.choice(numbers)

    while True:
        try:
            guess = int(input("Guess: "))
            prev = guess

            if guess < 1:
                continue
            elif guess < correct:
                print("Too small!")
            elif guess > correct:
                print("Too large!")
            else:
                return "Just right!"


        except ValueError:
            continue






main()


