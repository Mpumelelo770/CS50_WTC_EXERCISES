def convert(str):
    return str.replace(":)","🙂").replace(":(","🙁")

def main():
    sentence = input("Enter a sentence of your choice: ")
    print(convert(sentence))

main()