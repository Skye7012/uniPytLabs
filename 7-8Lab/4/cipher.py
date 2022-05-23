alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

def getKey(decr, enc):
	key = []
	for i in range(len(decr)):
		n = len(alphabet)
		encI = getIndex(enc[i])
		decI = getIndex(decr[i])
		t = (n - decI + encI) % n
		# t = abs(encI - decI)
		key.append(t)
	return key

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
# text = 'машинамолококолесосок'
# text = encrypt(text, 12984753623)
# print(text)
# print(encrypt('молоко', 12984753623))
# print(encrypt('машина', 12984753623))
# print(encrypt('колесо', 12984753623))
# print(encrypt('сок', 12984753623))

# decr = decrypt(text, 12984753623)
# print(decr)