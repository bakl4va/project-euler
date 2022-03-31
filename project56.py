def euler56():
    maxsum = 0
    for a in range(1, 100):
        for b in range(1, 100):
            tmp = pow(a, b)
            tmpls = [int(el) for el in str(tmp)]
            if maxsum < sum(tmpls):
                maxsum = sum(tmpls)
    return maxsum
print(euler56())

