class Human():
    def __init__(self, name, occupation, age, networth, city):
        self.name = name
        self.occupation = occupation
        self.age = age
        self.networth = networth
        self.city = city

    def information(self):
        print(f"{self.name} is a/an {self.occupation} his/her age is {self.age} his/her networth is {self.networth} and he/she is living in {self.city} ")

a = Human("Ali", "Businessman", 19, "150 MIllion Dollars", "Karachi")

b = Human("Aisha", "Entreprenuer", 23, "83 Million dollars", "Karachi")

c = Human("Muhammad Mirza", "Electronic Engineer", 19, "7.4 Million dollars", "Karachi" )

a.information()
b.information()
c.information()

