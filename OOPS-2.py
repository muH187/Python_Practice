class Person():
    def __init__(self, name, age, occupation, networth, city, country):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.networth = networth
        self.city = city
        self.country = country

    def details(self):
        print(f"{self.name} is a/an {self.occupation} his/her age is {self.age} his/her net-worth is {self.networth} and he/she is from {self.city},{self.country}")


Muhammad_Ali = Person("Muhammad Ali", 19,"Businessman", "157 Million Dollars", "Karachi", "Pakistan" )
Muhammad_Ali.details()

Aisha = Person("Aisha", 22, "Entreprenuer", "92 Million Dollars", "Karachi", "Pakistan")
Aisha.details()