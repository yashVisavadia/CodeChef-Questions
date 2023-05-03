# T = int(input())
# for _ in range(T):
#     n = int(input())
#     arr = list(map(int, input().split()))
#
#     cnt = 0
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             if arr[i] - arr[j] != arr[j] - arr[i]:
#                 cnt += 1
#
#     print(cnt)
from collections import defaultdict


def cal(i):
    if i == 1 or i == 0:
        return 0
    else:
        return int(i * (i - 1) / 2)
    return ans


T = int(input())
for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    ans = n * (n - 1) / 2
    ans = int(ans)

    dic = defaultdict(int)

    for i in arr:
        dic[i] += 1

    for k, v in dic.items():
        print(cal(v))
        cnt += cal(v)
    print(ans - cnt)
