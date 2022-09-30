# https://school.programmers.co.kr/learn/courses/15008/lessons/121686
import heapq

def solution(program):
    answer = []
    now = 0
    program = sorted(program, key=lambda x : x[1])
    started = []
    waiting_time = {i : 0 for i in range(1, 11)}
    while True :
        while program :
            if now < program[0][1] and not started:
                now = program[0][1]
                continue
            elif program[0][1] <= now :
                a, b, c = program.pop(0)
                heapq.heappush(started, (a, b, c))
                continue
            else :
                break
                
        progress = heapq.heappop(started)
        waiting_time[progress[0]] += now - progress[1]
        now += progress[2]
        if not program and not started :
            break
    answer.append(now)
    answer += waiting_time.values()
    return answer

if __name__=='__main__' :
    program = [[2, 0, 10], [1, 5, 5], [3, 5, 3], [3, 12, 2]]
    print(solution(program))