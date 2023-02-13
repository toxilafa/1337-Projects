import sys
import string

if len(sys.argv) != 3 or sys.argv[2].isdigit is False:
    print("ERROR\n")
    sys.exit()

argv = sys.argv[1]
punctuation = string.punctuation
for p in punctuation:
    argv = argv.replace(p, '')

result = argv.split(" ")
tmp = result[:]
for item in tmp:
    if len(item) <= int(sys.argv[2]):
        result.pop(result.index(item))

print(result)
