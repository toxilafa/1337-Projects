from asyncio import FastChildWatcher
import sys


def usage(condition):
    if condition is False:
        print("Usage: python operations.py <number1> <number2>\nExample:")
        print("\tpython operations.py 10 3")
        sys.exit()

    return


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


if len(sys.argv) > 3:
    print("InputError: too many arguments\n")
    usage(False)
elif len(sys.argv) != 3:
    usage(False)
elif is_number(sys.argv[1]) is False or is_number(sys.argv[2]) is False:
    print("InputError: only numbers\n")
    usage(False)
else:
    firstNumber = sys.argv[1]
    firstNumberEscapes = escape_sign(firstNumber)
    firstNumber = int(firstNumber[firstNumberEscapes:])
    secondNumber = sys.argv[2]
    secondNumberEscapes = escape_sign(secondNumber)
    secondNumber = int(secondNumber[secondNumberEscapes:])
    print("Sum:\t\t", firstNumber + secondNumber)
    print("Difference:\t", firstNumber - secondNumber)
    print("Product:\t", firstNumber * secondNumber)
    if int(secondNumber == 0):
        print("Quotient:\t", "ERROR (div by zero)")
    else:
        print("Quotient:\t", firstNumber / secondNumber)
    if int(secondNumber == 0):
        print("Remainder:\t", "ERROR (modulo by zero)")
    else:
        print("Remainder:\t", firstNumber % secondNumber)
