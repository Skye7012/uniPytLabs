res = 0
i = 1
prev = 0

def aFunc(n):
	return (2*n+n**2)/2**n

while True:
	new=aFunc(i)
	if(abs(new - prev) < 0.001):
		res+=new
		break
	res+=new
	prev=new
	i+=1

print("res = " + str(res))
