s = input("S = ")
s0 = input("S0 = ")

if (s0 in s):
	delS = s.find(s0)
	s = s[:delS] + s[delS + len(s0):]

print(s)