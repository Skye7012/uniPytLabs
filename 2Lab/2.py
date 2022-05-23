x = int(input("x = "))
y = int(input("y = "))

if (x < y):
	x,y = y,x

print("x =", x)
print("y =", y)