phrase = "The right format"

length = len(phrase)

print("%s%s" % ("".join('-' for i in range(42-length)), phrase[0:41]), end="")
