import sys


def text_analyzer(*arguments):

    upperCase = 0
    lowerCase = 0
    charaters = 0
    punctuation = 0
    spaces = 0
    total = 0

    if len(arguments) > 1:
        print("ERROR")
        sys.exit()
    elif len(arguments) == 0:
        argv = input("What is the text to analyse?\n>> ")
    else:
        argv = arguments[0]

    for index in argv:
        if index.islower():
            lowerCase += 1
        elif index.isupper():
            upperCase += 1
        elif index == '.' or index == ',' or index == '!' or index == '?':
            punctuation += 1
        elif index == ' ' or index == '\t':
            spaces += 1
        else:
            charaters += 1
        total += 1

    print("The text contains ", total, " characters:")
    print(" - ", upperCase, " upper letters")
    print(" - ", lowerCase, " lower letters")
    print(" - ", punctuation, " punctuation marks")
    print(" - ", spaces, " spaces")
