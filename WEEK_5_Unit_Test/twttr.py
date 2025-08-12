

def main():
    phrase = input("Enter any word: ")
    print(shorten(phrase))



def shorten(word):
    exclude = ["a", "e", "i", "o", "u"]
    new = ""
    for letter in word:
        if letter.lower() in exclude:
            continue
        new += letter

    return new

if __name__ == "__main__":
    main()



