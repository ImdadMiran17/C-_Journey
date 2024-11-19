# import numpy as np

def solve():
    n = int(input())
    arr = list(map(int, input().split(" ")))
    cnt = 0
    for i in range(n):
        if arr[i]%2 != 0:
            cnt += 1
    if cnt%2 == 0:
        print("YES")
    else:
        print("NO")


for _ in range(int(input())):
    solve()
