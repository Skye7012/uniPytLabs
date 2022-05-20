from functools import reduce
from tkinter.messagebox import RETRY

def IsTarget(num):
	numStr = str(num)
	nums = list(map(int, numStr))

	x = num**2
	y = reduce(lambda x,y: x**3+y**3, nums)
	isTr = num**2 == reduce(lambda x,y: x**3+y**3, nums)

	if (len(nums) != 3):
		print("Вы ввели не трехзначное число")
	else:
		if (isTr):
			return True
		else:
			return False

for n in range(0,1000):
	if(IsTarget(n)):
		print(n)

print("end")