
def findfiboseq():
    """Find the sequence of fibonnaci less than 4 million"""

    fibolist = [1, 2]

    while fibolist[-1] < 4000000:
        sequence = fibolist[-2] + fibolist[-1]
        fibolist.append(sequence)

    if fibolist[-1] > 4000000:
        fibolist.pop()

    # evenfibolist = []
    # for number in fibolist:
    #     if number % 2 == 0:
    #         evenfibolist.append(number)

    # print(evenfibolist)
    # return sum(evenfibolist)
    return sum([number for number in fibolist if number % 2 == 0])

print(findfiboseq())






































