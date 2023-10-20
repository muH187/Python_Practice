class Employee():
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def details(self):
        print(f"The name and id of Employee: {self.name} and {self.id}")


class Programmer(Employee):
    def showLanguage(self):
        print("The default Programming language is Python The Great:")

ep1 = Employee("Ali", 23)
ep1.details()

ep2 = Programmer("Aisha", 24)
ep2.details()
ep2.showLanguage()

