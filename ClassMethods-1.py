class Person:
    companyName = "Google"
    def showDetails(self):
        print(f"The name is {self.name}, age {self.age}, and the company is {self.companyName}")

    @classmethod
    def changeCompany(cls, newCompany):
        cls.companyName = newCompany


ep1 = Person()
ep1.name = "Ali"
ep1.age = 19
ep1.showDetails()
ep1.changeCompany("Apple")
ep1.showDetails()
print(Person.companyName)
