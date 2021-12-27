# https://www.acmicpc.net/problem/19236

import pprint

def draw_graph(fish_pos) :
    graph = [[0] * 4 for _ in range(4)]
    for i in range(1, 17) :
        r, c = fish_pos[i]
        graph[r][c] = i
    return graph

def can_move(fish_pos, fish_direct, idx) :
    graph = draw_graph(fish_pos)
    r_f, c_f = fish_pos[idx]
    dr_f, dc_f = direction[fish_direct[idx]]
    r_f = r_f + dr_f
    c_f = c_f + dc_f
    if 0 <= r_f < 4 and 0 <= c_f < 4 : # 공간 밖을 벗어나는지
        if graph[r_f][c_f] in range(1, 17) or graph[r_f][c_f] : # 움직일 위치에 다른 물고기 또는 빈공간인지
            return True
    return False  # 상어 또는 공간 밖이면

def turn_fish(direct) :
    direct += 1
    print(direct)
    if direct == 9 :
        direct = 1
    return direct


def move_fish(fish_pos, fish_direct) :
    for i in range(1, 16) :
        if fish_pos[i] : # 상어가 아니면 빈공간 빼기
            r_f, c_f = fish_pos[i]
            d_f = fish_direct[i]
        else :
            continue
        while True :
            if can_move(fish_pos, fish_direct, i) : # 움직일 수 있으면 위치 교환
                dr_f, dc_f = direction[fish_direct[i]]
                r_f2 = r_f + dr_f
                c_f2 = c_f + dc_f
                graph = draw_graph(fish_pos)
                temp = graph[r_f2][c_f2]
                fish_pos[i], fish_pos[temp] = fish_pos[temp], fish_pos[i]
                print(i, '**')
                break
            else : # 움직일 수 없으면 회전
                d_f = turn_fish(d_f)
                fish_direct[i] = d_f
                print(fish_direct)




direction = [False, (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]


fish_pos = [True] * 17
graph = []
fish_direct = [False] * 17

for i in range(4) :
    temp = list(map(int, input().split()))
    for j in range(0, 8, 2) :
        fish_pos[temp[j]] = (i, j // 2)
        fish_direct[temp[j]] = temp[j + 1]
print(fish_direct)
move_fish(fish_pos, fish_direct)
print(fish_pos)
pprint.pprint(graph, width = 20)


