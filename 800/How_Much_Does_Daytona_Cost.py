def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt=0
    for _ in arr:
        if k in arr:
            cnt+=1
    if cnt>=1:
        print("YES")
    else:
        print("NO")

for _ in range(int(input())):
    solve()
