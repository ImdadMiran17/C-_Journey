# import numpy as np

def solve():
    n = int(input())
    arr = list(map(int, input().split(" ")))
    xor = 0
    for x in arr:
        xor ^= x
    if xor == 0:
        print(0)
    else:
        if n % 2 == 1:
            print(xor)
        else:
            print(-1)
 
        
    

for _ in range(int(input())):
    solve()
