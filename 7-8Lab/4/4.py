import cipher

path = "7-8Lab/4/text.txt"
pathTarget = "7-8Lab/4/done.txt"

with open(path, 'r', encoding='utf-8') as file:
	text = file.readlines()

text = [i.strip('\n') for i in text]
len = len(text[0])

def checkText(text):
	for i in text:
		if(len(i) > len):
			print("Неверный текст")
			return False
	return True

key = cipher.getKey(text[0], text[1])
key = list(map(str,key))
key = ''.join(key)
key = int(key)

with open(pathTarget, 'w', encoding='utf-8') as file:
	for i in text[2:]:
		decr = cipher.decrypt(i,key)
		file.write(decr + "\n")