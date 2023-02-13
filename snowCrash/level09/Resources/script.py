import sys

def modify(str):
        length = len(str) - 1
        i = 0
        result = ""
        while i < length:
                c = ord(str[i]) - i
                result += chr(c)
                i += 1
        print result

f = open(sys.argv[1], "r")
modify(f.read())
