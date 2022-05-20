class PcPart:
	type = "Undefined"

	def __init__(self, name, cost):
		self.__name = name
		self.__cost = cost

	@property
	def name(self):
		return self.__name

	@property
	def cost(self):
		return self.__cost


	@name.setter
	def name(self,name):
		self.__name = name

	@cost.setter
	def cost(self,cost):
		self.__cost = cost

	def __str__(self):
		text = f"name = {self.name}"
		text += f", cost = {self.cost}"
		return text