def solution(number, k):
    answer = []
    answer.append(number[0])
    for i in number[1:] :
        while answer[-1] < i and k > 0 :
            answer.pop()
            k -= 1 
            if not answer or k <= 0 :
                break
        answer.append(i)
        if len(answer) == len(number) - k :
            break
    return ''.join(answer)


if __name__ == '__main__' : 
    number = "2131234"
    k = 3
    print(solution(number, k))