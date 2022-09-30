# https://school.programmers.co.kr/learn/courses/30/lessons/70129
def solution(s):
    cnt = 0
    turn_cnt = 0
    while s != '1' :
        turn_cnt += 1
        cnt += s.count('0')
        s = s.replace('0','')
        s = str(bin(len(s)))[2:]
    return [turn_cnt, cnt]

if __name__=='__main__' :
    s = "110010101001"
    print(solution(s))