def main():
    answer = input("What is the the answer to the Great Question of Life, the Universe and Everything?")
    if answer.strip() == "42" or answer.lower() == "forty-two" or answer.lower() == "forty two":
        print("Yes")
    else:
        print("No")

main()

#Can also use match-case syntax for this