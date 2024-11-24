# import numpy as np
import math

def solve():
    n = int(input())
    arr = list(map(int, input().split(" ")))
    gcd = 1e6
    for i in range(n):
        for j in range(i+1, n):
            gcd = min(math.gcd(arr[i], arr[j]), gcd)
    
    if gcd > 2:
        print("NO")
    else:
        print("YES")


for _ in range(int(input())):
    solve()
