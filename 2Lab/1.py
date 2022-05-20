x = float(input("x = "))
res = 0

if(x >= -7):
	res = -x**2
else:
	res = (2**(-x))/(x**2-9)

print("res = ", res)