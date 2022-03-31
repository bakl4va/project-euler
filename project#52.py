def euler52_good():
    for i in range(2, 20000000):
        i_str = sorted(str(i))
        my_list = [sorted(str(i * j)) for j in range(2, 7)]
        if all(i_str == x for x in my_list):
            return i
    return 'not found'

print(euler52_good())







