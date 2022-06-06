from typing import overload


def func():
    pass

class Cls:
    pass

class Person:
    # static
    __aff = "Goott"

    def __init__(self, name="", age=""):
        # field
        self.__name  = name
        self.__age   = age
    
    def __str__(self):
        return "[Person] name={0}, age={1}".format(self.__name, self.__age)

    def __eq__(self, other):
        if(self.__class__ == other.__class__):    
            return self.__name == other.__name and self.__age == other.__age
        return False

    def __lt__(self, other):
        if(self.__class__ == other.__class__):    
            return self.__age < other.__age
        return False

    def __gt__(self, other):
        if(self.__class__ == other.__class__):    
            return self.__age > other.__age
        return False

    def __le__(self, other):
        if(self.__class__ == other.__class__):    
            return self.__age <= other.__age
        return False

    def __ge__(self, other):
        if(self.__class__ == other.__class__):    
            return self.__age >= other.__age
        return False

    @staticmethod # decorator
    def getAff(): # self 필요 없음
        return Person.__aff

    def getName(self):
        #print("getName")
        return self.__name
    
    def getAge(self):
        #print("getAge")
        return self.__age

    def setName(self, name):
        #print("setName")
        self.__name = name
    
    def setAge(self, age):
        #print("setAge")
        self.__age = age

p1 = Person('sally', 30) # __init__()
print(p1) # __str__()
print(p1.getName())
print(p1.getAge())
p1.setName("sally2")
p1.setAge(40)

p1_copy = Person('sally', 30) # __init__()
print(p1_copy) # __str__()
print(p1_copy.getName())
print(p1_copy.getAge())
p1_copy.setName("sally2")
p1_copy.setAge(40)


p2 = Person('kelly', 50) # __init__()
print(p2) # __str__()
print(p2.getName())
print(p2.getAge())
p2.setName("kelly2")
p2.setAge(40)

# == 연산자 overloading (__eq__)
print(p1 == p1_copy)

# > 연산자 overloading (__gt__)
print(p1 > p1_copy)

# >= 연산자 overloading (__ge__)
print(p1 >= p1_copy)

# < 연산자 overloading (__lt__)
print(p1 < p1_copy)

# <= 연산자 overloading (__le__)
print(p1 <= p1_copy)

print(Person.getAff())

#############################################
# class inheritance (상속)

from multipledispatch import dispatch

class Employee(Person): # Employee extends Person
    @dispatch(str, str, str)
    def __init__(self, name, age, department) -> None: 
        super().__init__(name, age)
        self.department = department 
    
    @dispatch(Person, str)
    def __init__(self, person, department) -> None: 
        super().__init__(person.getName(), person.getAge())
        self.department = department  

    def __str__(self) -> str:
        return super().__str__().replace("Person", "Employee") \
        + " , department = {0}".format(self.department)

emp = Employee("sally", "30", "engineer")
print(emp)

emp = Employee(p1, "engineer")
print(emp)

#############################################
# polymorphism (다형성)
def add(a, b):
    return a + b

class Animal:
    def cry(self):
        print('.....')

class Dog(Animal):
    # override
    def cry(self):
        print('멍멍!')

class Cat(Animal):
    # override
    def cry(self):
        print('야옹!')

# List<Animal> animals = {new Dog(), new Cat(), new Animal()}
animals = [Dog(), Cat(), Animal()] # 다형성
for animal in animals:
    animal.cry()

a = 10
a = "abc"