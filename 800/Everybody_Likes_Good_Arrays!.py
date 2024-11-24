# import numpy as np

def solve():
    n = int(input())
    arr = list(map(int, input().split(" ")))
    pair = 0
    for i in range(n-1):
        if arr[i] % 2 == 0 and arr[i+1] % 2 == 0:
            pair += 1
        if arr[i] % 2 == 1 and arr[i+1] % 2 == 1:
            pair += 1

    print(pair)


for _ in range(int(input())):
    solve()
