prop = input("")

text = """class Stomatology:
	def __init__(self, name, addres, 
	surname, {prop}):
		self.__name = name
		self.__addres = addres
		self.__surname = surname
		self.{prop} = {prop}

	@property
	def name(self):
		return self.__name

	@property
	def addres(self):
		return self.__addres

	@property
	def surname(self):
		return self.__surname
	
	@name.setter
	def name(self,name):
		self.__name = name

	@addres.setter
	def addres(self,addres):
		self.__addres = addres

	@surname.setter
	def surname(self,surname):
		self.__surname = surname

	def __str__(self):
		text = f"name = {self.name}"
		text += f", addres = {self.addres}"
		text += f", surname = {self.surname}"
		return text"""

text = text.expandtabs(4)
print(text)