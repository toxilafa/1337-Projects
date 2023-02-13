import sys

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----',  'a': '.-', 'b': '-...',
    'c': '-.-.', 'd': '-..', 'e': '.',
    'f': '..-.', 'g': '--.', 'h': '....',
    'i': '..', 'j': '.---', 'k': '-.-',
    'l': '.-..', 'm': '--', 'n': '-.',
    'o': '---', 'p': '.--.', 'q': '--.-',
    'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--',
    'x': '-..-', 'y': '-.--', 'z': '--..', ' ': ''}


def encrypt(args):
    cipher = ''
    for letter in args:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += '/ '
    return cipher


def check(str):
    values = []
    for item in MORSE_CODE_DICT:
        values += item
    for arg in str:
        for item in arg:
            if item not in values:
                print("ERROR")
                sys.exit()


check(sys.argv[1:])
for argv in sys.argv[1:]:
    print(encrypt(argv), end=" ")

if len(sys.argv) > 1:
    print("")
