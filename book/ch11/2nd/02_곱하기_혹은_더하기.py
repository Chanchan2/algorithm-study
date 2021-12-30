number_list = list(input())
number_list = [int(i) for i in number_list]
answer = 0
for i in number_list :
    answer = max(answer + i , answer * i)
print(answer)
