from collections import defaultdict

import math

mod = 1000000007
T = int(input())
# for _ in range(T):
# n = int(input())

dic = defaultdict(int)
for __ in range(T):
    x, y = map(int, input().split())
    dic[x] += 1

p = 1
for i in dic:
    p *= math.factorial(dic[i])

q = math.factorial(T)
qinv = pow(q, mod - 2, mod)
ans = (p * qinv) % mod
print(ans)
