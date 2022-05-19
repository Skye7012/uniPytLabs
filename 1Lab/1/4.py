try:
	k = int(input("K = "))
	
	if(k < 1 or k > 365):
		raise Exception("1<=K<=365 !")

	shift = 1
	res = (k + shift) % 7
	if(res == 0):
		res=7
	print("res = " + str(res))

except Exception as e:
	print(e)