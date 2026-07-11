# OOP Concepts in Python
Name: Krishu Kumar

# 1. Encapsulation

class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance

    def show_balance(self):
        print("Current Balance:", self.__balance)

account = BankAccount("Krishu", 5000)
print("Account Holder:", account.holder)
account.show_balance()

# 2. Abstraction

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        print("Area of Square:", self.side * self.side)

square = Square(5)
square.area()

# 3. Inheritance

class Vehicle:

    def start(self):
        print("Vehicle Started")

class Bike(Vehicle):

    def ride(self):
        print("Bike is Running")

bike = Bike()
bike.start()
bike.ride()
# 4. Polymorphism

class Cat:

    def sound(self):
        print("Cat says Meow")

class Cow:

    def sound(self):
        print("Cow says Moo")

animals = [Cat(), Cow()]

for animal in animals:
    animal.sound()
