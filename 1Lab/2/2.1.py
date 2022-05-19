try:
	num = int(input("num = "))
	numStr = str(num)
	num = [int(i) for i in numStr]
	a = int(input("a = "))
	z = int(input("z = "))
	
	if(a < 0 or a > 8):
		raise Exception("0<=a<=8 !")

	if(z < 2 or z > 5):
		raise Exception("2<=z<=4 !")

	aCount = [i for i in num if i == a]
	aCount = len(aCount)
	zCount = [i for i in num if i%z==0]
	zCount = len(zCount)
	aBiggerCount = [i for i in num if i > a]
	aBiggerCount = len(aBiggerCount)

	print(str(aCount) + " раз в num встречается цифра а")
	print(str(zCount) + "  цифр, кратных z")
	print("сумма его цифр, больших a = " + str(aBiggerCount))

except Exception as e:
	print(e)