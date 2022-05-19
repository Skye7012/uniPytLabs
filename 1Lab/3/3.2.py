n = int(input("n = "))
nums = []
count = 1

for i in range(n):
	nums.append(float(input(str(i) + " element = ")))	

incr = nums[0] > nums[1]
def compare(i):
	if(incr):
		return nums[i] > nums[i+1]
	else:
		return nums[i] < nums[i+1]

for i in range(n-1):
	if(not compare(i)):
		incr = not incr
		count += 1

print("count = " + str(count))