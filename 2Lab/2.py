x = []
y = []

xLen = int(input("x length = "))
for i in range(xLen):
	x.append(int(input(str(i+1) + " element = ")))	

yLen = int(input("y length = "))
for i in range(yLen):
	y.append(int(input(str(i+1) + " element = ")))	

all = x + y
max = max(all)
min = min(all)

if(max not in x):
	iMax = y.index(max)
	iMin = x.index(min)
	y[iMax],x[iMin] = x[iMin], y[iMax]

print("x = ", x)
print("y = ", y)