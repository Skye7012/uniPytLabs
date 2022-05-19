from functools import reduce


n = int(input("n = "))
nums = []

for i in range(n):
	nums.append(float(input(str(i) + " element = ")))	

k1 = int(input("k1 = "))
k2 = int(input("k2 = "))

if(k1<0 or k2>n-1):
	raise('Неправильные индексы')

res = nums[k1:k2+1]
# res = sum(res)
res = reduce(lambda x,y: x + y, res)
print(res)