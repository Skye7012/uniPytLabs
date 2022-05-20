from functools import reduce

print("Введите трехзначное число")
num = int(input("n = "))
numStr = str(num)
nums = list(map(int, numStr))

isTr = num**2 == reduce(lambda x,y: x**3+y**3, nums)

if (len(nums) != 3):
	print("Вы ввели не трехзначное число")
else:
	if (isTr):
		print(True)
	else:
		print(False)
