import random
import sys


def generator(text, sep=" ", option=None):
    if type(text) is str:
        result = text.split(sep)
    else:
        print("ERROR")
        sys.exit()
    if option is None:
        for item in result:
            yield item
    elif option == "shuffle":
        randomlist = random.sample(range(0, len(result)), len(result))
        newResult = []
        for i in randomlist:
            newResult.append(result[i])
        result = newResult[:]
        for item in result:
            yield item
    elif option == "unique":
        newResult = []
        for item in result:
            if item not in newResult:
                newResult.append(item)
        result = newResult[:]
        for item in result:
            yield item
    elif option == "ordered":
        result.sort()
        for item in result:
            yield item
    else:
        print("ERROR")
        sys.exit()


# if __name__ == '__main__':
#     TEXT = "Le Lorem Ipsum est simplement du faux texte."

#     print("Regular split :")
#     for i in generator(TEXT):
#         print(i)
#     print()

#     print("Split with sep :")
#     for i in generator(TEXT, sep="a"):
#         print(i)
#     print()

#     print("Shuffle split :")
#     for i in generator(TEXT, option="shuffle"):
#         print(i)
#     print()

#     print("Unique split :")
#     for i in generator("a a b c a b c a b b c a", option="unique"):
#         print(i)
#     print()

#     print("Ordered split :")
#     for i in generator(TEXT, option="ordered"):
#         print(i)
#     print()

#     print("Invalid split :")
#     for i in generator(TEXT, option="invalid"):
#         print(i)
#     print()

#     print("Invalid split :")
#     for i in generator(6):
#         print(i)
#     print()
