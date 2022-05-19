a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))

a = a > 0
b = b > 0
c = c > 0
statements = [a,b,c]

res = [i for i in statements if i in [True]]
res = len(res)

if(res == 1):
	print("Ровно одно из чисел A, B, C положительное")
else:
	print("Не выполняется условие \"Ровно одно из чисел A, B, C положительное\"")
