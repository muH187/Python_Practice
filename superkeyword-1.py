# class ParentClass:
#     def parent_method(self):
#         print("This is a parent class")
#
# class ChildClass(ParentClass):
#     def child_method(self):
#         print("This is a child class")
#         super().parent_method()
#
#
# child = ChildClass()
# child.child_method()

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, language):
        super().__init__(name,id)
        self.language = language

mirza = Employee("Muhammad Mirza", "234")
print(mirza.name)
print(mirza.id)

ali = Programmer("Muhammad Ali", "2345", "Python")
print(ali.name)
print(ali.id)
print(ali.language)