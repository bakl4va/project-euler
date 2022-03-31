
def prime_list(max_num):
    primes = []
    for i in range(2, max_num):
        for j in primes:
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes


print(sum(prime_list(25)))
