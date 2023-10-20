class People:
    name = "Harry"
    occupation = "Software Developer"
    net_worth = 10
    def information(self):
        print(f"{self.name} is a {self.occupation} and his net-worth is {self.net_worth}")

a = People()
b = People()
c = People()
d = People()
e = People()
f = People()
g = People()


b.name = "Muhammad Mirza"
b.occupation = "Electronical Engineer"
b.net_worth = "1.2 Million Dollars"

c.name = "Muhammad Umer"
c.occupation = "Businessman"
c.net_worth = "30 Million Dollars"

d.name = "Abdul Wali"
d.occupation = "Businessman"
d.net_worth = "3.9 Million Dollars"

e.name = "Bilal Farhan"
e.occupation = "Computer Scientist"
e.net_worth = "1.1 Million Dollars"

f.name = "Muhammad Ali"
f.occupation = "Entreprenuer"
f.net_worth = "2.8 Billion Dollars"

g.name = "Abdul Basit"
g.occupation = "Economist"
g.net_worth = "550 Million Dollars"

a.information()
b.information()
c.information()
d.information()
e.information()
f.information()
g.information()
