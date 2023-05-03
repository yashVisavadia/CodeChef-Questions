def cmp(n):
    global C
    ans = ''
    s = '0' * 32 + bin(n)[2:]
    s = s[-C:]
    for i in s:
        if i == '0':
            ans += '1'
        else:
            ans += '0'
    a = 0
    k = 0
    for i in ans[::-1]:
        if i == '1':
            a += 2 ** k
        k += 1
    return a


T = int(input())
for _ in range(T):
    A, B, C = map(int, input().split())

    print(cmp(B))
    A = cmp(B)
    print(A | C - A & B)

