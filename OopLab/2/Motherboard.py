from PcPart import PcPart

class Motherboard(PcPart):
	type = "Motherboard"

	def __init__(self, name, cost,
	socket, formFactor):
		super().__init__(name, cost)
		self.__socket = socket
		self.__formFactor = formFactor

	@property
	def socket(self):
		return self.__socket

	@property
	def formFactor(self):
		return self.__formFactor


	@socket.setter
	def socket(self,socket):
		self.__socket = socket

	@formFactor.setter
	def formFactor(self,formFactor):
		self.__formFactor = formFactor

	def __str__(self):
		text = f"type = {self.type}"
		text += ", " + super().__str__()
		text += f", socket = {self.socket}"
		text += f", formFactor = {self.formFactor}"
		return text

mb = Motherboard("Asus 12", 1244, "LGA1700", "microATX")
print(mb)