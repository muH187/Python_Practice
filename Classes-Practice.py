class Animal:
    alive = True

class Dog(Animal):
    def eat(self):
        print("The dog is eating food.")

class Cat(Animal):
    def sleep(self):
        print("This cat is sleeping peacefully.")

class Eagle(Animal):
    def fly(self):
        print("This Eagle is flying.")

dog = Dog()
dog.eat()

cat = Cat()
print(cat.alive)

eagle = Eagle()
eagle.fly()


class Employee:
    def __init__(self, name, age, profession, city, country, networth):
        self.name = name
        self.age = age
        self.profession = profession
        self.city = city
        self.country = country
        self.networth = networth

    def showDetails(self):
        print(f'This is {self.name}, who is {self.age} years old, {self.profession} living in {self.city} {self.country} and his/her networth is {self.networth}')

employee1 = Employee('Muhammad Ali','19', 'Businessmen', 'Karachi','Pakistan','255 Million Dollars')
employee1.showDetails()

employee2 = Employee('Muhammad Mirza','19','Electrical Engineer', 'Karachi', 'Pakistan', '125 Million Dollars')
employee2.showDetails()

employee3 = Employee('Aisha', 22, 'Entrepreneur', 'Karachi', 'Pakistan', '150 Million Dollars')
employee3.showDetails()

