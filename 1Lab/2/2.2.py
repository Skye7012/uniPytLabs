n = int(input("num = "))
num = 1

for i in range(n):
	num *= (2*i + 1)/(2*(i+1))

print("res = " + str(num))