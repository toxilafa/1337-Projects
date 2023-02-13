import sys


def escape_sign(str):
    escapes = 0
    for sign in str:
        if (sign == '-' or sign == '+'):
            escapes += 1

    return escapes


def is_number(str):
    escapes = escape_sign(str)
    for i in range(escapes, len(str)):
        if str[i].isdigit() is False:
            return False
    return True


if len(sys.argv) == 1:
    sys.exit()

if (len(sys.argv) > 2 or is_number(sys.argv[1]) is False):
    print("ERROR")
    sys.exit()
escapes = escape_sign(sys.argv[1])
number = int(sys.argv[1][escapes:])

if (number == 0):
    print("I'm Zero.")
elif (number % 2 == 0):
    print("I'm Even.")
else:
    print("I'm Odd.")
