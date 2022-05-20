from math import tan


w = float(input("w = "))

if(w!=0 and 1/tan(w)<0.5):
	w=-w
elif(w == 0):
	w = 1

print("res = ", w)