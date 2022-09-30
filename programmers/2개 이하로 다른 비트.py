def solution(numbers):
    answer = []
    for number in numbers :
        rest = number % 4
        if rest  <= 2 :
            answer.append(number + 1)
        else :
            temp = '0' + bin(number)[2:]
            for i in range(len(temp)-1, -1, -1):
                if temp[i] == '0':
                    answer.append(int(temp[0:i] + "10" + temp[i+2:],2))
                    break
    return answer

if __name__ == '__main__' :
    numbers = [2,7]
    print(solution(numbers))