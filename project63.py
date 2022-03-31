def euler63():
    count = 0
    for num in range(1, 25):
        for exp in range(1, 25):
            if len(str(pow(num, exp))) == exp:
                count += 1
            elif len(str(pow(num, exp))) < exp:
                continue
            else:
                break
    return count
print(euler63())
