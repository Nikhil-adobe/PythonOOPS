# parent class
# class Person(object):
#     def __init__(self, name, idnumber):
#         self.name = name
#         self.idnumber = idnumber

#     def display(self):
#         print(self.name)
#         print(self.idnumber)
        
#     def details(self):
#         print("My name is {}".format(self.name))
#         print("IdNumber: {}".format(self.idnumber))
    
# # child class
# class Employee(Person):
#     def __init__(self, name, idnumber, role):
#         self.role = role

#         Person.__init__(self, name, idnumber)
        
#     def details(self):
#         print("My name is {}".format(self.name))
#         print("IdNumber: {}".format(self.idnumber))
#         print("Role: {}".format(self.role))

# a = Employee('Nikhil', 23, "Apprentice")

# a.display()
# a.details()





# Inheritance
# class Car(object):
#     def __init__(self, type, color, comapny):
#         self.type = type
#         self.color = color
#         self.comapny = comapny
    
#     def displayDetails(self):
#         print("Type of Car is -> {}".format(self.type))
#         print("Car color -> {}".format(self.color))
#         print("Car company ", self.comapny)

# class Suzuki(Car):
#     def details(self):
#         print(self.type)
#         print(self.color)
#         print(self.comapny)

# class Punch(Car):
#     def details(self):
#         print(self.type)
#         print(self.color)
#         print(self.comapny)

# c1 = Suzuki('Manual', 'White', 'Maruti Suzuki')
# c1.displayDetails()

# c2 = Punch('Automatic', 'Gray', 'Tata')
# c2.details()
        

# Polymorphism

class Animal:
    def walk(self):
        print("Can walk")
    
    def fly(self):
        print("Can fly")
    
class dog(Animal):
    def fly(self):
        print("Cannot fly")

class kangaroo(Animal):
    def walk(self):
        print("Cannot walk")
    
    def fly(self):
        print("Cannot fly")

o1 = Animal()
o2 = dog()
o3 = kangaroo()

print("Parent Class")
o1.fly()
o1.walk()

print("Child classes")
o2.fly()
o2.walk()