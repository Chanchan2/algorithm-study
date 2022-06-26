# https://www.acmicpc.net/problem/1620

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
poke_dict = {}
num_dict = {}
for i in range(n) :
    pokemon = input().strip()
    poke_dict[pokemon] = i+1
    num_dict[i+1] = pokemon

for i in range(m) :
    q = input().strip()
    if q.isdigit() :
        print(num_dict[int(q)])
    else :
        print(poke_dict[q])