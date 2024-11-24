# import numpy as np

def solve():
    n = int(input())
    arr = list(map(int, input().split(" ")))
    if arr[0] == arr[n-1]:
        print("NO")
    else:
        print("YES")
        print(arr[n-1], end=" ")
        print(*arr[0:n-1])


for _ in range(int(input())):
    solve()
