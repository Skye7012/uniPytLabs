class Person:
	def __init__(self, name, surname):
		self.__name = name
		self.__surname = surname
  
	@property
	def name(self):
		return self.__name

	@property
	def surname(self):
		return self.__surname

	@name.setter
	def name(self,name):
		self._name = name
  
	@surname.setter
	def surname(self,surname):
		self._surname = surname

	def display(self):
		print("I am person\n" + str(self))
  
	def __str__(self):
		return f"name = {self.name}, surname = {self.surname}"
  

class Student(Person):
	def __init__(self, name, surname, course):
		super().__init__(name, surname)
		self.course = course
    
	def display(self):
		print("I am student")
		print(self)
		# print(super().__str__())
		# print("course = ", self.course)
  
	def __str__(self):
		return super().__str__() + ", course = " + str(self.course)
  
class Worker(Person):
	def display(self):
		print("I am worker")
		print(super().__str__())
  

person = Person("Саша", "Колыванов")
person.display()
student = Student("Маша", "Васильева", 3)
student.display()
worker = Worker("Васлий", "Иванов")
worker.display()