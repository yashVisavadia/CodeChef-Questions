from math import floor, sqrt

T = int(input())
for _ in range(T):
    X = int(input())

    if X == 1:
        print(0)
        continue

    i = floor(sqrt(X))
    if sqrt(X) == i:
        if X - i * (i - 1) > 10 ** 6 or X - i * (i - 1) < 1:
            print(-1)
            continue
        print(i, i - 1,  X - i * (i - 1))
        continue

    if X - i**2 > 10 ** 6 or X - i*i < 1:
        print(-1)
        continue

    print(i, i, X - i**2)
