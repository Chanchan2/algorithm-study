# https://programmers.co.kr/learn/courses/30/lessons/60062
import copy

def solution(n, weak, dist):
    dist.sort(reversed = True)
    friends = dist
    answer = int(1e9)
    for i in weak :
        temp_weak = copy.deepcopy(weak)
        temp_weak.remove(i)
        cnt = 1
        friend = friends.pop(0)
        for j in range(n) :
            friend -= 1
            pos = i + j
            if pos >= n :
                pos -= n
            if pos in temp_weak :
                weak.remove(pos)
                cnt += 1
            if not temp_weak :
                answer = min(answer, cnt)
                break
            if friend == 0 and friends :
                friend = friends.pop(0)
            elif friend == 0 and not friends :
                break
    if answer == int(1e9) :
        answer = -1
    return answer