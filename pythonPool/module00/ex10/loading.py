from ast import YieldFrom
import sys
import time
from timeit import default_timer as timer
import timeit
from datetime import timedelta

t = time.time()
elap = 0


def ft_progress(lst):
    test = 0
    for item in lst:
        elapsed_time = time.time()
        percent = (item * 100 / len(lst))
        equals = percent / 5
        print("ETA: %2.2fs [ %.2d%%][%-20s] %d/%d | elapsed time %.2fs" % (
            time.time() - t,
            percent,
            "".join("=" for x in range(int(equals))) + ">",
            item, len(lst), elap + (time.time() - elapsed_time)), end="\r")
        test = (time.time() - elapsed_time) * 30
        yield item, test
    print("\n...", end="")


listy = range(3333)
ret = 0
for elem, test in ft_progress(listy):
    ret += elem
    elap += test
    time.sleep(0.005)
print()
print(ret)
