def amicableNumber(limit):
    factorList = []
    amicablePairs = []
    sum1 = 0
    for a in range(2, limit):
    # finding factors not including itself
        for b in range(1, a):
            if a % b == 0 and a != b:
                factorList.append(b)
        possibleAmicable = sum(factorList)
        factorList.clear()
        if checkAmicable(possibleAmicable, a):
            amicablePairs.append(a)
    return sum(amicablePairs)


def checkAmicable(possible, number):
    factorList = []
    for b in range(1, possible):
        if possible % b == 0 and possible != b and possible > 0:
            factorList.append(b)
    if number == sum(factorList and number != possible):
        factorList.clear()
        return True
    else:
        factorList.clear()
        return False

print(amicableNumber(10000))

