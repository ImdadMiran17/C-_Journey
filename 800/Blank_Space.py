# import numpy as np

def solve():
    n = int(input())
    arr = list(map(int, input().split(" ")))
    blank = 0
    res = 0
    for i in range(n):
        if arr[i] == 1:
            res = max(res, blank)
            blank = 0
        else:
            blank += 1
    print(max(res, blank))
        
    

for _ in range(int(input())):
    solve()
