# https://school.programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    fibo = [0, 1]
    for i in range(100000) :
        fibo.append((fibo[-1]+fibo[-2]) % 1234567)
    answer = fibo[n]
    return answer

if __name__=='__main__' :
    n = 3
    print(solution(n))