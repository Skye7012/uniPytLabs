s = input("S = ")
alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"

def isTextValid(text):
	for char in text:
		if(char not in alphabet):
			raise Exception("Неправильный символ, используйте только буквы русского алфавита")

try:
	isTextValid(s)

	first = ord(alphabet[0])
	last = ord(alphabet[-1])
	n = len(alphabet)

	def getIndex(char):
		return alphabet.find(char)+1

	def getChar(index):
		return alphabet[index-1]

	def encrypt(s):
		sNew = ""
		for char in s:
			res = n - getIndex(char) + 1
			sNew += getChar(res)
		return sNew

	def decrypt(s):
		sNew = ""
		for char in s:
			res = abs(getIndex(char) - n) + 1 
			sNew += getChar(res)
		return sNew

	enc = encrypt(s)
	print(enc)

	dec = decrypt(enc)
	print(dec)
except Exception as e:
	print(e)
