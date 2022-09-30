# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    if max(citations)  == 0 :
        return 0
        
    for h in range(max(citations)) :
        answer = sum([1 for i in citations if h <= i])
        if answer < h :
            return h - 1


if __name__ == '__main__' :
    citations = [0, 0, 0, 0, 0]
    print(solution(citations))