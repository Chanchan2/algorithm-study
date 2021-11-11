g = int(input())
p = int(input())

parent = list(range(g + 1))
parent = [i if i == 1 else i - 1 for i in parent]
print(parent)
occupy = [True] * (g + 1)

cnt = 0
end = False
planes = []
for _ in range(p) :
    planes.append(int(input()))

for plane in planes :
    temp = plane
    while True :
        if occupy[temp] :
            occupy[temp] = False
            cnt += 1
            break
        else :
            temp = parent[temp]
        if temp == 1 and not occupy[temp] :
            end = True
            break
    if end :
        break

print(cnt)