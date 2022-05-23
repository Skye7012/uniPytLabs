n = int(input("n = "))
i = 0
prev = 0
incr = True

def isSaw(now):
	if(incr and now > prev):
		return True
	elif(not incr and now < prev):
		return True
	else:
		return False

for j in range(n):
	now = float(input(str(j+1) + " element = "))
	i += 1
	if(j == 1):
		incr = True if now > prev else False
	if(not isSaw(now) and i > 1):
		break
	prev = now
	incr = not incr

print(i-1)

