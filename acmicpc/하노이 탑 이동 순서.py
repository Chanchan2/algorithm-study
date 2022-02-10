# https://www.acmicpc.net/problem/11729

import sys

input = sys.stdin.readline

n = int(input())

def move(num) :
    
    if num == 1 :
        return [(1, 3)]

    else:
        pre_move = move(num - 1)
        result = []
        for a, b in pre_move :
            if a == 2 :
                a_2 = 3
            elif a == 3 :
                a_2 = 2
            else :
                a_2 = 1
            
            if b == 2 :
                b_2 = 3
            elif b == 3 :
                b_2 = 2
            else :
                b_2 = 1

            result.append((a_2, b_2))

        result.append((1, 3))

        for a, b in pre_move :
            if a == 1 :
                a_2 = 2
            elif a == 2 :
                a_2 = 1
            else :
                a_2 = a
            
            if b == 1 :
                b_2 = 2
            elif b == 2 :
                b_2 = 1
            else :
                b_2 = b
            
            result.append((a_2, b_2))

        return result

answer = move(n)

print(len(answer))
for a, b in answer :
    print(a, b)