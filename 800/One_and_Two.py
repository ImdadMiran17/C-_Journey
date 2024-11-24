# import numpy as np

def solve():
    n = int(input())
    arr = list(map(int, input().split(" ")))
    sm, total, res = 0, 0, 0
    for i in range(n):
        sm += arr[i] == 2
    
    for i in range(n):
        total += arr[i] == 2
        if total == sm - total:
            res = i+1
            break
        else:
            res = -1

    print(res)


for _ in range(int(input())):
    solve()
