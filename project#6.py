
def sumSquare1():
    list1=[]
    x = 1
    for i in range(100):
        list1.append(x)
        x += 1
    squares = []
    for number in list1:
        squares.append(pow(number, 2))
    addition = sum(squares)
    print(addition)

def sumSquare2():
    list1 = []
    x = 1
    for i in range(100):
        list1.append(x)
        x += 1
    addition = sum(list1)
    result = pow(addition, 2)
    print(result)

sumSquare1()
sumSquare2()