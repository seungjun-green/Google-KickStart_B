from math import sqrt
from itertools import count, islice

def isPrimeNumber(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))

def solution(Z):
    res = 1
    middle = sqrt(Z)
    middle = int(middle)
    possible = []
    count = 0
    # two smaller one
    for i in range(middle, 1, -1):
        isPrime = isPrimeNumber(i)

        if isPrime:
            possible.append(i)

        if len(possible) == 2:
            break



    count = 0
    for i in range(middle+1, 10**18+1):
        isPrime = isPrimeNumber(i)

        if isPrime:
            possible.append(i)
            break

    if len(possible) == 2:
        return possible[0] * possible[1]

    b = possible[0] * possible[2]
    c = possible[0] * possible[1]

    if c <= Z and b > Z:
        return c
    if b <= Z:
        return b


t = int(input())
for i in range(1,t+1):
    temp = input().split()
    temp = temp[0]
    Z = int(temp)
    res = solution(Z)
    print("Case #{}: {}".format(i, res))


