def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    res = abs(arr[0])
    for i in range(n):
        if arr[i] == 0:
            res = 0
            break
        res = min(res, abs(arr[i]))

    print(res)


# for _ in range(int(input())):
solve()
