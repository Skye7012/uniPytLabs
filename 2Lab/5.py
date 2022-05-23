a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

nums = [a,b,c]

max = max(nums)
min = min(nums)

a = max
c = min

def main():
	if(not(a + b > c and b + c > a and c + a > b)):
		print("Такого треугольника сущестовать не может")
		return

	if(a**2==b**2+c**2):
		print("Прямоугольный")
	elif(a**2<b**2+c**2):
		print("Остроугольный")
	elif(a**2>b**2+c**2):
		print("Тупоугольный")

	if(a==b==c):
		print("Равносторонний")
	elif(len(set(nums)) == 2):
		print("Равнобедренный")
	else:
		print("Разносторонний")

main()