def solve():
    target = [
        [1,1,1,1,1,1,1,1,1,1],
        [1,2,2,2,2,2,2,2,2,1],
        [1,2,3,3,3,3,3,3,2,1],
        [1,2,3,4,4,4,4,3,2,1],
        [1,2,3,4,5,5,4,3,2,1],
        [1,2,3,4,5,5,4,3,2,1],
        [1,2,3,4,4,4,4,3,2,1],
        [1,2,3,3,3,3,3,3,2,1],
        [1,2,2,2,2,2,2,2,2,1],
        [1,1,1,1,1,1,1,1,1,1],
    ]

    player = []
    score = 0
    for _ in range(10):
        player.append(list(input()))
    
    for i in range(10):
        for j in range(10):
            if player[i][j] == 'X':
                score += target[i][j]

    print(score)



for _ in range(int(input())):
    solve()
