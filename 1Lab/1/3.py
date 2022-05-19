from math import sqrt

try:
	a = int(input("a = "))
	b = int(input("b = "))
	c = int(input("c = "))
	x = int(input("x = "))
	
	if(x == 0):
		raise Exception("x не должен быть равен 0")

	d = b**2 - 4*a*c

	if(d < 0):
		raise Exception("Отрицательный дискриминант")

	if(d == 0):
		x1 = -b/2*a
		print("x1 = " + str(x1))
	else:
		x1 = (-b + sqrt(d))/2*a
		x2 = (-b - sqrt(d))/2*a
		print("x1 = " + str(x1))
		print("x2 = " + str(x2))

except Exception as e:
	print(e)