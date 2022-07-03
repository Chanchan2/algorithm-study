# https://programmers.co.kr/learn/courses/30/lessons/81302

def check_wall(p1, p2, graph) :
    r1, c1 = p1
    r2, c2 = p2
    if r1 == r2 or c1 == c2 :
        if graph[(r1 + r2) // 2][(c1 + c2) // 2] == 'X' :
            return False
    elif graph[r1][c2] == 'X' and graph[r2][c1] == 'X' :
        return False
    return True

def check_ok(points, graph) :
    for i in range(len(points)) :
        p1 = points[i]
        for j in range(i, len(points)) :
            p2 = points[j]
            distance = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
            if distance == 1 :
                return 0
            elif distance == 2 and check_wall(p1, p2, graph) :
                    return 0
    return 1
    
def solution(places):
    answer = []
    for place in places :
        graph = [list(row) for row in place]
        points = []
        for r in range(5) :
            for c in range(5) :
                if graph[r][c] == 'P' :
                    points.append((r, c))
        answer.append(check_ok(points, graph))
    return answer


if __name__ == '__main__' :
    places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
            ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
            ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
            ["OOOXX", "XOOOX", "OOPXX", "OXOOX", "OOPOO"], 
            ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
    print(solution(places))