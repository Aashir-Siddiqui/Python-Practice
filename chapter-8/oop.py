from abc import ABC, abstractmethod

class Student:
    course = "py"
    fees = 10000

s1 = Student()

print(s1.course, s1.fees)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def welcomeUser(self):
        print(f"Welcome {self.name}!")
        
        
p1 = Person("Aashir", 18)
print(p1.name, p1.age)
del p1.age
print(p1.name)
p1.welcomeUser()
    
    
class Calculator:
    def add(self, a, b):
        return a + b
    def multi(self, a, b):
        return a * b

c1 = Calculator()

print(c1.add(2, 5))
print(c1.multi(2, 5))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split(",")
        return cls(name, int(age))

p = Person.from_string("Aashir,22")
print(p.name, p.age)


class Demo:
    x = 10

    def instance_method(self):
        return self.x

    @classmethod
    def class_method(cls):
        return cls.x

    @staticmethod
    def static_method():
        return "Utility function"

d1 = Demo()
print(d1.instance_method())
print(d1.class_method())
print(d1.static_method())


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

p = Employee("Ali", 22)
print(p)


class Abc:
    def __repr__(self):
        return "Abc()"

    def __str__(self):
        return "This is Demo object"

a = Abc()
print(a)


class Bank_Account:
    def __init__(self, balance):
        self.__balance = balance
    def deposite(self, amount):
        self.__balance += amount
    def getBalance(self):
        return self.__balance

acc = Bank_Account(1000)
acc.deposite(500)
print(acc.getBalance())
        
        
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass


class Bike(Vehicle):
    def start(self):
        print("Bike start with kick")
        
class Car(Vehicle):
    def start(self):
        print("Car started with key")


b = Bike()
c = Car()

b.start()
c.start()


class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
d.bark()


class Bird:
    def fly(self):
        print("Bird flies")

class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")

b = Penguin()
b.fly()
