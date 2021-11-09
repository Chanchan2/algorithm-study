def score(a, b) :
    n = min(len(a), len(b))
    scr = [ 1 if a[i] == b[i] else 0 for i in range(n)]
    return sum(scr)

a = list(input())
b = list(input())

cnt = 0
idx = 0
while a != b :
    


