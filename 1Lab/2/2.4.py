num = int(input("num = "))
numStr = str(num)
num = list(map(int,numStr))
bools = []

def isSaw(i):
	a = num[i-1]
	b = num[i]
	c = num[i+1]
	return a < b and b > c or a > b and b < c

for i in range(1,len(num)-1):
	bools.append(isSaw(i))

try:
	print(bools.index(False)+1)
except:
	print(0)

