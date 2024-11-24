# import numpy as np

def solve():
    n = input()
    res = 0
    l = len(n)  
    res += int(n[0])
    l -= 1
    res += 9*l

    print(res)



for _ in range(int(input())):
    solve()
