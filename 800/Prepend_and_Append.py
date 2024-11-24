# import numpy as np

def solve():
    n = int(input())
    # arr = list(map(int, input().split(" ")))
    s = input()
    l = 0
    r = n-1
    ans = n
    while s[l] != s[r] and ans > 0:
        ans -= 2
        l += 1
        r -= 1
    print(ans)


for _ in range(int(input())):
    solve()
