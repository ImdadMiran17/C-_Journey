# import numpy as np

def solve():
    n = int(input())
    arr = list(map(int, input().split(" ")))
    for i in range(n):
        print(n+1-arr[i], end=" ")
    print()
for _ in range(int(input())):
    solve()
