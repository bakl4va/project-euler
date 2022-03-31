def euler55():
    leest = [num for num in range(1, 10000)]
    hashtbl = [1] * (len(leest) + 1)
    hashtbl[0] = 0
    for el in leest:
        for iterate in range(0, 50):
            if iterate == 0:
                tmp = el + int(str(el)[::-1])
            else:
                tmp = tmp + int(str(tmp)[::-1])
            tmp1 = int(str(tmp)[::-1])
            if tmp == tmp1 and len(str(tmp)) > 1:
                hashtbl[el] = 0
                break
    lychrel = [i for i, el in enumerate(hashtbl) if el]
    return len(lychrel)
print(euler55())