# import numpy as np

def solve():
    n = int(input())
    arr = list(map(int, input().split(" ")))
    diff = 1e9
    if arr != sorted(arr):
        print(0)
    elif arr[0] == arr[n-1]:
        print(1)
    else:
        for i in range(1,n):
            diff = min(arr[i]-arr[i-1], diff)
        print((diff//2)+1)


for _ in range(int(input())):
    solve()
