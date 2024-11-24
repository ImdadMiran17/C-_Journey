# import numpy as np

def solve():
    n,a,b = map(int,input().split(" "))
    res = (n == a and n == b) or (a+b+2 <= n)
    print("YES" if res else "NO")



for _ in range(int(input())):
    solve()
