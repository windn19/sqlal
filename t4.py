from math import sqrt, ceil


def prime_num(n):
    a = set(range(2, n + 1))
    for i in range(2, ceil(sqrt(n))):
        b = set(range(i * i, n + 1, i))
        a -= b
    return ' '.join(map(str, a))


n = int(input())
numbers = [True] * (n + 1)
for i in range(2, n + 1):
    if numbers[i]:
        for j in range(2 * i, n + 1, i):
            numbers[j] = False
for i in range(2, n + 1):
    if numbers[i]:
        print(i, end=' ')
