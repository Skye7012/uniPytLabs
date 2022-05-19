from math import log, sqrt


def calculate_y():
	a = int(input("a = "))
	b = int(input("b = "))
	x = int(input("x = "))
	y = (2*a-4*b)/(3*a+6*b)  - (x**3 - 1)/(x**2 - 1)
	print("y = " + str(y))

def calculate_z():
	x = int(input("x = "))
	z = log(x)**3 + 3*log(x)
	print("z = " + str(z))

def calcucate_quadratic_equation():
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

def main():
	#calculate_y()
	#calculate_z()
	calcucate_quadratic_equation()


main()