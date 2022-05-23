path = "7-8Lab/1/1.txt"

with open(path, 'r') as file:
	nums = file.read()
	nums = nums.split()
	nums = [i for i in nums if nums.index(i)%2==0]
	
with open(path, 'w') as file:
	file.write(' '.join(nums))

print('done')

