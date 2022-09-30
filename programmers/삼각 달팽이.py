def solution(n):
    answer = [[0] * i for i in range(1, n+1)]
    way = [(1, 0), (0, 1), (-1, -1)]
    idx = 0
    x, y = -1 ,0
    step = n
    num = 1
    while n :
        idx %= 3
        dx, dy = way[idx][0], way[idx][1]
        for _ in range(step) :
            x, y = x+dx, y+dy
            print(x, y)
            answer[x][y] = num
            num += 1
        n -= 1
        idx += 1
        step -= 1
    return sum(answer, [])


if __name__=='__main__' :
    n = 4
    print(solution(n))