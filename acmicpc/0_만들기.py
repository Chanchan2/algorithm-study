# https://www.acmicpc.net/problem/7490

import sys
import itertools as it

input = sys.stdin.readline

operater =['+', '-', ' ']


def cal(array) :
    temp = ''.join(list(map(str, array)))
    temp = temp.replace(' ', '')
    result = eval(temp)
    return result

      
def  make_zero(n) :
    answer = []
    op_list = list(it.product(operater, repeat = n - 1))
    for i in range(len(op_list)) :
        temp = list(it.chain(*zip(range(1, n), op_list[i]))) + [n]
        if cal(temp) == 0 :
            answer.append(temp)
    
    return answer
        

lines = int(input())


for i in range(lines) :
    n = int(input())
    answer = make_zero(n)
    answer.sort()
    for l in answer :
        print(''.join(list(map(str, l))))

    else :
        print()
