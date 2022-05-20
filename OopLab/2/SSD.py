from PcPart import PcPart

class SSD(PcPart):
	type = "SSD"

	def __init__(self, name, cost,
	capacity, readSpeed, writeSpeed):
		super().__init__(name, cost)
		self.__capacity = capacity
		self.__readSpeed = readSpeed
		self.__writeSpeed = writeSpeed

	@property
	def capacity(self):
		return self.__capacity

	@property
	def readSpeed(self):
		return self.__readSpeed

	@property
	def writeSpeed(self):
		return self.__writeSpeed


	@capacity.setter
	def capacity(self,capacity):
		self.__capacity = capacity

	@readSpeed.setter
	def readSpeed(self,readSpeed):
		self.__readSpeed = readSpeed

	@writeSpeed.setter
	def writeSpeed(self,writeSpeed):
		self.__writeSpeed = writeSpeed

	def __str__(self):
		text = f"type = {self.type}"
		text += ", " + super().__str__()
		text += f", capacity = {self.capacity}"
		text += f", readSpeed = {self.readSpeed}"
		text += f", writeSpeed = {self.writeSpeed}"
		return text

ssd = SSD("Samsung 970 Evo Plus 1", 9650, 1024, 1800, 1100)
print(ssd)