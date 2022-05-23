try:
	num = int(input("num = "))
	len = len(str(num))
	a = int(input("a = "))
	z = int(input("z = "))
	
	if(a < 0 or a > 8):
		raise Exception("0<=a<=8 !")

	if(z < 2 or z > 5):
		raise Exception("2<=z<=4 !")

	aCount, zCount, aBiggerCount = 0,0,0

	x = len
	while (x != 0):
		x = int(num / 10)
		y = num % 10
		aCount = aCount + 1 if y == a else aCount
		zCount = zCount + 1 if y % z == 0 else zCount
		aBiggerCount = aBiggerCount + 1 if y > a else aBiggerCount
		num = x

	print(str(aCount) + " раз в num встречается цифра а")
	print(str(zCount) + "  цифр, кратных z")
	print("сумма его цифр, больших a = " + str(aBiggerCount))

except Exception as e:
	print(e)