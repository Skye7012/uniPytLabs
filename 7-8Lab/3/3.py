path = "7-8Lab/3/text.txt"

with open(path, 'r') as file:
	text = file.read()

print(text)
	
with open(path, 'w') as file:
	text = text.split()
	text.reverse()
	text = min(text, key=len)
	file.write(text)

print(text)
print('done')