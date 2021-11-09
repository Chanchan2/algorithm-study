n = int(input())
ugly_nums =[1]

idx = 0
while len(ugly_nums) <= n :
    num = ugly_nums[idx]
    ugly_nums.append(num * 2)
    ugly_nums.append(num * 3)
    ugly_nums.append(num * 5)
    ugly_nums = list(set(ugly_nums))
    ugly_nums = sorted(ugly_nums)
    idx += 1

print(ugly_nums[n - 1])