import math
import random


def findtriplet():
    """Find the three triplets, add them together, if sum = 1000, print product."""
    a = 0
    b = 0
    c = 0
    while a + b + c != 1000: # 10k $ for this line.
        a = random.randint(1, 200)
        b = random.randint(200, 400)
        cc = math.pow(a, 2) + math.pow(b, 2)
        c = math.sqrt(cc)

        # print(a, b, c)
    print(int(a * b * c))


findtriplet()