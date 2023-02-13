import sys

all_args = ""

for arg in sys.argv[1:]:
    all_args += arg
    all_args += ' '

for caracter in all_args[::-1]:
    if caracter.isupper():
        print(caracter.lower(), end='')
    elif caracter.islower():
        print(caracter.upper(), end='')
    else:
        print(caracter, end='')

print('')
