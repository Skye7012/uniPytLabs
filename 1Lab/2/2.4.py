n = int(input("n = "))
nums = []

for i in range(n):
	nums.append(float(input(str(i) + " element = ")))

bools = []

def isSaw(i):
	a = nums[i-1]
	b = nums[i]
	c = nums[i+1]
	return a < b and b > c or a > b and b < c

for i in range(1,len(nums)-1):
	bools.append(isSaw(i))

if(False in bools):
	print(bools.index(False)+1)
else:
	print(0)

