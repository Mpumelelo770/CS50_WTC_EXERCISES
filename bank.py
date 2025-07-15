def main():
    greeting = input("Greeting:")
    spaceless = greeting.strip().lower()
    if spaceless[0] == "h" and spaceless[0:5] != "hello":
        print("$20")
    elif spaceless[0:5] == "hello":
        print("$0")
    else:
        print("$100")

main()