# https://school.programmers.co.kr/learn/courses/30/lessons/12951
def solution(s):
    letter_list = list(s.lower())
    for i in range(len(letter_list)) :
        if i == 0 or s[i-1] == ' ' :
            if s[i].isalpha() :
                letter_list[i] = letter_list[i].upper()
    answer = ''.join(letter_list)
    return answer

if __name__=='__main__' :
    s = "for the last week"
    print(solution(s))