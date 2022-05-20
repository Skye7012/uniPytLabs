from PcPart import PcPart

class CPU(PcPart):
	type = "CPU"

	def __init__(self, name, cost,
	socket, coreCount, clockRate):
		super().__init__(name, cost)
		self.__socket = socket
		self.__coreCount = coreCount
		self.__clockRate = clockRate

	@property
	def socket(self):
		return self.__socket

	@property
	def coreCount(self):
		return self.__coreCount

	@property
	def clockRate(self):
		return self.__clockRate


	@socket.setter
	def socket(self,socket):
		self.__socket = socket

	@coreCount.setter
	def coreCount(self,coreCount):
		self.__coreCount = coreCount

	@clockRate.setter
	def clockRate(self,clockRate):
		self.__clockRate = clockRate

	def __str__(self):
		text = f"type = {self.type}"
		text += ", " + super().__str__()
		text += f", socket = {self.socket}"
		text += f", coreCount = {self.coreCount}"
		text += f", clockRate = {self.clockRate}"
		return text

cpu = CPU("i3-12100", 1244, "LGA1700", 4, 3300)
print(cpu)