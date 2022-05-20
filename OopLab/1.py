from datetime import date


class Stomatology:
	def __init__(self, name, addres, 
	surname, policeNum, treatDate,
	doctorName, workDescription, serviceSum):
		self.__name = name
		self.__addres = addres
		self.__surname = surname
		self.__policeNum = policeNum
		self.__treatDate = treatDate
		self.__doctorName = doctorName
		self.__workDescription = workDescription
		self.__serviceSum = serviceSum

	@property
	def name(self):
		return self.__name

	@property
	def addres(self):
		return self.__addres

	@property
	def surname(self):
		return self.__surname

	@property
	def policeNum(self):
		return self.__policeNum

	@property
	def treatDate(self):
		return self.__treatDate

	@property
	def doctorName(self):
		return self.__doctorName

	@property
	def workDescription(self):
		return self.__workDescription

	@property
	def serviceSum(self):
		return self.__serviceSum


	@name.setter
	def name(self,name):
		self.__name = name

	@addres.setter
	def addres(self,addres):
		self.__addres = addres

	@surname.setter
	def surname(self,surname):
		self.__surname = surname

	@policeNum.setter
	def policeNum(self,policeNum):
		self.__policeNum = policeNum

	@treatDate.setter
	def treatDate(self,treatDate):
		self.__treatDate = treatDate

	@doctorName.setter
	def doctorName(self,doctorName):
		self.__doctorName = doctorName

	@workDescription.setter
	def workDescription(self,workDescription):
		self.__workDescription = workDescription

	@serviceSum.setter
	def serviceSum(self,serviceSum):
		self.__serviceSum = serviceSum


	def __str__(self):
		text = f"name = {self.name}"
		text += f", addres = {self.addres}"
		text += f", surname = {self.surname}"
		text += f", policeNum = {self.policeNum}"
		text += f", treatDate = {self.treatDate}"
		text += f", doctorName = {self.doctorName}"
		text += f", workDescription = {self.workDescription}"
		text += f", serviceSum = {self.serviceSum}"
		return text

stomatology = Stomatology("РСП", "Улица Пушкина", "Васнецова",
	1222423, date(2022, 5, 10), "Васильев",
	"Пломбирование", 9999)

print(stomatology)