# import numpy as np

def solve():
    n = int(input())
    arr = list(map(int, input().split(" ")))
    cnt = 0
    sum = 0
    for i in range(n):
        if arr[i] == -1:
            cnt += 1
    
    while cnt> n-cnt:
        cnt -= 1
        sum += 1
    
    print(sum + (cnt%2))


    
for _ in range(int(input())):
    solve()
