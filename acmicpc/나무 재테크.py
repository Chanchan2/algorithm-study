# https://www.acmicpc.net/problem/16235

import sys

input = sys.stdin.readline


def aging(pos) :  # 봄, 여름
    r, c = pos 
    i = 0
    temp = 0
    while True :
        if trees[pos][i] <= land[r][c] :
            land[r][c] -= trees[pos][i]
            trees[pos][i] += 1
            i += 1

        else :
            temp += trees[pos][i] // 2
            del trees[pos][i]
        
        if len(trees[pos]) <= i :
            land[r][c] += temp
            break
        
        
def breeding(pos) : #가을
    r, c = pos
    for i in range(len(trees[pos])) :
        if trees[pos][i] % 5 == 0 :
            for x, y in b :
                r_n = r + y
                c_n = c + x
                if r_n in range(n) and c_n in range(n) :
                    trees[(r_n, c_n)].insert(0, 1)
    

def fertilizing() : # 겨울
    for r in range(n) :
        for c in range(n) :
            land[r][c] = land[r][c] + a[r][c]

def year () :
    for r in range(n) :
        for c in range(n) :
            if trees[(r, c)] :
                aging((r, c))

    for r in range(n) :
        for c in range(n) :
            if trees[(r, c)] :
                breeding((r, c))

    fertilizing()


n, m, k = map(int, input().split())
a = []    # 양분
trees = {}    # 나무
land = [[5] * n for _ in range(n)]
for r in range(n) :
    for c in range(n) :
        trees[(r, c)] = []
b = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for i in range(n) :
    a.append(list(map(int, input().split())))

for i in range(m) :
    x, y, z = map(int, input().split())
    trees[(x - 1,y - 1)].append(z)

for _ in range(k) :
    year()

result = 0
for r in range(n) :
    for c in range(n) :
        result += len(trees[(r, c)])



print(result)