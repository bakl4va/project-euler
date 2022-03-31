def findFractions():
    # Stores fraction results

    fractiondic = []
    splitnumbers = []

    for i in range(2, 10):
        operation = 1 / i
        fractiondic.append(operation)

    for number in fractiondic:
        number_string = str(number)
        split_contents = number_string.split()
        splitnumbers.append(split_contents)

    print(fractiondic)
    print(splitnumbers)

findFractions()




