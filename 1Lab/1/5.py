a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))

a = a > 0
b = b > 0
c = c > 0

res = (a and not b and not c) or (not a and b and not c) or (not a and not b and c)

if(res):
	print("Ровно одно из чисел A, B, C положительное")
else:
	print("Не выполняется условие \"Ровно одно из чисел A, B, C положительное\"")
