alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

def getIndex(char):
	return alphabet.find(char)+1

def getChar(index):
	index %= len(alphabet)
	return alphabet[index-1]

def getKeyByIndex(key, keyIndex):
	key = str(key)
	key = list(map(int,key))
	ln = len(key)
	i = keyIndex if keyIndex < ln else keyIndex % len(key)
	return key[i]

def encrypt(text, key):
	chars = list(text)
	for i in range(len(chars)):
		letter = getIndex(chars[i]) + getKeyByIndex(key, i)
		chars[i] = getChar(letter)
	return ''.join(chars)

def decrypt(text, key):
	chars = list(text)
	for i in range(len(chars)):
		letter = getIndex(chars[i]) - getKeyByIndex(key, i)
		chars[i] = getChar(letter)
	return ''.join(chars)

# text = encrypt('абвгдежзийклмнопрстуфхцчшщъыьэюя', 1234)
# print(text)
# decr = decrypt(text, 1234)
# print(decr)
text = 'машинамолококолесосок'
print(encrypt(text, 12984753623))