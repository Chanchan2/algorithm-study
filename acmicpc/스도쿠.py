# https://www.acmicpc.net/problem/2580

ver = [[] for _ in range(9)]
hor = [[] for _ in range(9)]
square = [[] for _ in range(9)]
spots = []
for r in range(9) :
    temp = list(map(int, input().split()))
    hor[r] = temp
    for c in range(9) :
        ver[c].append(temp[c])
        if temp[c] == 0 :
            spots.append((r, c))
    square[3*(r//3)].extend(temp[:3])
    square[3*(r//3) + 1].extend(temp[3:6])
    square[3*(r//3) + 2].extend(temp[6:])

zeros = [False] * len(spots)

def check (pos, num) :
    r, c = pos
    result = False
    if num in hor[r] or num in ver[c] or num in square[3 * (r//3) + c//3] :
        return False
    return True

def dfs(idx) :
    if idx == len(spots) :
        for i in range(9) :
            print(*hor[i])
        exit(0)

    for i in range(1, 10) :
        r, c = spots[idx]

        if check((r, c), i) :
            hor[r][c] = i
            dfs(idx + 1)
            hor[r][c] = 0

dfs(0)
