# import numpy as np

def solve():
    x,k = map(int, input().split(" "))
    if x%k != 0:
        print(1)
        print(x)
    else:
        print(2)
        print(1, x-1)
    


for _ in range(int(input())):
    solve()
