class Person:
 
    def __init__(self, name):
        self.__name = name   # имя человека
 
    @property
    def name(self):
        return self.__name
 
    def display_info(self):
        print(f"Name: {self.__name}")
 
class Employee(Person):
 
    def __init__(self, name, company):
        super().__init__(name)
        self.company = company
 
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Company: {self.company}")
 
    def work(self):
        print(f"{self.name} works")
 
 
alsu = Employee("Alsu", "Microsoft")
alsu.display_info()  # Name: Alsu
                    # Company: Microsoft
