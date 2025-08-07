

import emoji

def main():
    word = input()
    print(imoji(word))




def imoji(sentence):
    return emoji.emojize(sentence, language = 'alias')

main()
