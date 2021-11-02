T = int(input())
def dynamic(r, c) :
    if c == 0 :
        miner[r][c] = mine[r][c]
    else :
        if r == 0 :
            miner[r][c] = max(miner[r][c - 1], miner[r + 1][c - 1]) + mine[r][c]
        elif r == n - 1 :
            miner[r][c] = max(miner[r - 1][c - 1], miner[r][c - 1]) + mine[r][c]
        else :
            miner[r][c] = max(miner[r - 1][c - 1], miner[r][c - 1], miner[r + 1][c - 1]) + mine[r][c]
for t in range(T) :
    n, m = map(int,input().split())
    temp = list(map(int, input().split()))
    mine = [temp[i:i + m] for i in range(0, len(temp), m)]
    miner = [[0] * m for _ in range(n)]
    
    answer = 0

    for c in range(m) :
        for r in range(n) :
            dynamic(r, c)
            answer = max(answer, miner[r][c])
    # print(mine)
    print(answer)