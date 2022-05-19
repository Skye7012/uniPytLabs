n = int(input("n = "))
nums = []

for i in range(n):
	nums.append(int(input(str(i) + " element = ")))	

delItems = []
delIndeces = []
incr = nums[0] > nums[1]

def isSame(i):
	return nums[i-1] == nums[i+1]

for i in range(1,n-1):
	if(isSame(i)):
		delItems.extend([nums[i-1], nums[i+1]])
		delIndeces.extend([i-1,i+1])

delItems = set(delItems)
delIndeces = set(delIndeces)

q = 0

def isDelItem(i):
	if(nums[i-q] in delItems):
		delItems.remove(nums[i-q])
		return True
	return False

for i in delIndeces:
	if(not isDelItem(i)):
		nums.pop(i-q)
		q+=1

print("nums = " + str(nums))