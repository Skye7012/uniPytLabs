try:
	k = int(input("K = "))
	
	if(k < 1 or k > 365):
		raise Exception("1<=K<=365 !")

	shift = 1
	res = k % 7 + shift
	print("res = " + str(res))

except Exception as e:
	print(e)