# https://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 0
    for i in range(1, n+1) :
        temp = i
        a = 0
        while a < n :
            a += temp
            temp += 1
        if a == n :
            answer += 1
    return answer

if __name__=='__main__' :
    n = 15
    print(solution(n))