def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    res = 0
    for i in arr:
        res += i
    print(res*-1)

    
for _ in range(int(input())):
    solve()
