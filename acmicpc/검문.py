# https://www.acmicpc.net/problem/2981

import sys 

input = sys.stdin.readline

def get_gcd(a, b) :
    if a < b :
        a, b = b, a
    r= a % b
    if r != 0 :
        return get_gcd(b, r)
    else :
        return b

n = int(input())
num_list = []
for i in range(n) :
    num_list.append(int(input()))
num_list = sorted(num_list)
diff_list = [num_list[i] - num_list[i - 1] for i in range(1, len(num_list))]
gcd = diff_list[0]
for i in diff_list[1:] :
    gcd = get_gcd(gcd, i)

result = set()
for i in range(2, int(gcd**0.5) + 1) :
    if gcd % i == 0 :
        result.add(i)
        result.add(gcd // i)
result.add(gcd)
print(*sorted(list(result)))