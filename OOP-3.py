class Car:
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("The "+self.model+" is driving")

    def stop(self):
        print("The "+self.model+" is stopped")

car_1 = Car("Toyota","Corola",2022,"White")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)
car_1.drive()
car_1.stop()

car_2 = Car("Hyundai", "Sonata", 2023, "Offwhite")
print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)
car_2.drive()
car_2.stop()