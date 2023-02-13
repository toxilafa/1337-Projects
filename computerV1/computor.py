import sys
import re

regex = "[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?\*X\^\d?|\-\d|\+\d"

def my_abs(value):
    if value <= 0:
        return value * -1
    return value * 1

def swapSignAfterEqual(equation):
    beforeEqual = equation.split("=")[0]
    afterEqual = equation.split("=")[1]
    afterEqual = re.findall(regex, afterEqual)
    result = []
    for item in afterEqual:
        if not item.startswith("-"):
            if item.startswith("+"):
                result.append(item.replace("+", "-"))
            else:
                result.append("-" + item)
        else:
            result.append(item.replace("-", "+"))
    final = ""
    for item in result:
        final += item
    return beforeEqual + final

def getPolyDegree(equation):
    max = 0
    for item in equation:
        result = re.findall("\^\d?", item)
        if result:
            if int(result[0][1:]) > max:
                max = int(result[0][1:])
    return max

def reduceFormat(equation, degree):
    holder = []
    final = []
    while degree >= 0:
        strdegree = "% s" % degree
        result = 0
        for item in equation:
            if item.find("*X^" + strdegree) != -1:
                result += float(item[:item.find("*X^" + strdegree)])
                strresult = "% s" % result
        final.append(strresult + "*X^" + strdegree)
        degree -= 1
    degit = 0
    for item in equation:
        if item.find("*X^") == -1:
            degit += float(item)
    if degit != 0:
        final.append("% s" % degit)
    
    result = ""
    length = len(final)
    for i in range(0, length):
        if i == 0:
            result += final[0]
            continue
        if i + 1 < length:
            if final[i + 1].startswith("-"):
                result += "-"
            if not final[i + 1].startswith("-"):
                result += "+"
        else:
            if final[i].startswith("-"):
                result += "-"
            else:
                result += "+"
        if final[i].startswith("-"):
            result += final[i][1:]
        if not final[i].startswith("-"):
            result += final[i]
    result = result.replace("*", " * ")
    if result.startswith("-"):
        result = result[1:].replace("-", " - ")
        result = '-' + result
    else:
        result = result.replace("-", " - ")
    result = result.replace("+", " + ")

    result += " = 0"
    return result, final


def simpleSolution(equation):
    b, c = 0, 0
    for item in equation:
        if item.find("X^1") != -1:
            b = float(item[0:item.find("*X^1")])
        if item.find("X^0") != -1:
            c = float(item[0:item.find("*X^0")])
        if item.find("X") == -1:
            c += float(item)
    if b == 0 and c != 0:
        print("There is no solution for the equation.")
        return
    if b == 0 and c == 0:
        print("Each real number is a solution.")
        return
    x = c / b
    print("The solution is:")
    print("%f" % x)

def equationSolution(equation):
    a, b, c = 0, 0, 0
    for item in equation:
        if item.find("X^2") != -1:
            a = float(item[0:item.find("*X^2")])
        if item.find("X^1") != -1:
            b = float(item[0:item.find("*X^1")])
        if item.find("X^0") != -1:
            c = float(item[0:item.find("*X^0")])
        if item.find("X") == -1:
            c += float(item)
    delta = (b ** 2) - (4 * a * c)
    if a != 0:
        if delta > 0:
            x1 = (b * -1 + (delta ** (1/2))) / (2 * a)
            x2 = (b * -1 - (delta ** (1/2))) / (2 * a)
            print("Discriminant is strictly positive, the two solutions are:")
            print("%f.6" % x2)
            print("%f.6" % x1)
        if delta < 0:
            x2 = "% f" % (-b / (2 * a)) + ' - ' + "%f" % ((my_abs(delta) ** (1/2)) / (2 * a)) + ' * i'
            x1 = "% f" % (-b / (2 * a)) + ' + ' + "%f" % ((my_abs(delta) ** (1/2)) / (2 * a)) + ' * i'
            print("Discriminant is strictly negative, the two solutions are:")
            print(x1)
            print(x2)
        if delta == 0:
            x = -b / (2 * a)
            print("Discriminant is 0, the solution is:")
            print(x)
    else:
        simpleSolution(equation)

test = "5 * X^0 + 3 * X^1 + 3 * X^2 = 1 * X^0 + 0 * X^1"
str = ""
if len(sys.argv) == 2:
    if sys.argv[1] is not None:
        str = sys.argv[1]
if str == "":
    str = input()
str = str.replace(" ", "")
str = swapSignAfterEqual(str)
rr = re.findall(regex, str)
degree = getPolyDegree(rr)
result = reduceFormat(rr, degree)
if degree == 2:
    print("Reduced form: ", result[0])
    print("Polynomial degree: ", degree)
    equationSolution(result[1])
elif degree == 1:
    print("Reduced form: ", result[0])
    print("Polynomial degree: ", degree)
    simpleSolution(result[1])
if degree > 2:
    print("Reduced form: ", result[0])
    print("Polynomial degree: ", degree)
    print("The polynomial degree is strictly greater than 2, I can't solve.")
if degree == 0:
    simpleSolution(result[1])