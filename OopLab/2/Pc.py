from Motherboard import Motherboard
from CPU import CPU
from SSD import SSD

class PC:
	def __init__(self, parts):
		self.__parts = parts

	@property
	def parts(self):
		return self.__parts


	@parts.setter
	def parts(self,parts):
		self.__parts = parts

	def addPart(self, part):
		self.parts.append(part)

	def __str__(self):
		text = f"PC parts:\n"

		for part in self.parts:
			text += f"\t{part.__str__()}\n"

		return text

mb = Motherboard("Asus 12", 1244, "LGA1700", "microATX")
cpu = CPU("i3-12100", 1244, "LGA1700", 4, 3300)
ssd = SSD("Samsung 970 Evo Plus 1", 9650, 1024, 1800, 1100)
parts = [mb,cpu,ssd]

pc = PC(parts)
print(pc)

ssd2 = SSD("Samsung 980 Pro", 14589, 2048, 2800, 1600)
pc.addPart(ssd2)
print(pc)

