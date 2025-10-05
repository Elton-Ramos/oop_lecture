# Lecture Note: Object-Oriented Programming in Python

# 🎯 Objectives
# By the end of this lecture, students will be able to:
# - Understand the basic concepts of OOP.
# - Define and use classes and objects in Python.
# - Implement encapsulation, inheritance, and polymorphism.
# - Apply constructors, instance methods, class methods, and static methods.

# 1. 🧠 What is Object-Oriented Programming?
# Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects," which can contain:
# - Data in the form of attributes (also called fields or properties).
# - Code in the form of methods (functions associated with the object).

# 2. 🧱 Core Concepts of OOP
# - Class: A blueprint for creating objects (a factory).
# - Object: An instance of a class.
# - Encapsulation: Hiding internal state and requiring all interaction to be performed through methods.
# - Inheritance: Mechanism for creating new classes using existing classes.
# - Polymorphism: Ability to use the same method name in different ways.

# 3. 📦 Defining a Class and Creating Objects
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        return f"{self.name} says Woof!"

# Creating objects
dog1 = Dog("Buddy", "Golden Retriever")
print(dog1.bark())  # Output: Buddy says Woof!

# 4. 🔐 Encapsulation
# Encapsulation is achieved using private variables (convention: _ for protected, __ for private).
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def get_balance(self):
        return self.__balance

acct = BankAccount("Alice", 1000)
acct.deposit(500)
print(acct.get_balance())  # Output: 1500

# 5. 🧬 Inheritance
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

cat = Cat("Whiskers")
print(cat.speak())  # Output: Whiskers says Meow!

# 6. 🧩 Polymorphism
# Polymorphism allows the same method name to work differently depending on the object.
animals = [Dog("Rex", "Bulldog"), Cat("Whiskers")]
for animal in animals:
    print(animal.speak())
# Output:
# Rex says Woof!
# Whiskers says Meow!

# 7. 🛠 Class vs Static Methods
class Circle:
    pi = 3.1416
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return Circle.pi * self.radius * self.radius
    
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)
    
    @staticmethod
    def unit_circle():
        return Circle(1)

c = Circle.from_diameter(10)
print(c.area())  # Uses class method

# Class Method vs Static Method
# - @classmethod: Takes cls (refers to the class itself), operates on the class (can access/modify class variables)
# - @staticmethod: Takes no special first argument, utility functions that don’t access class or instance data

class Shape:
    def __init__(self, name):
        self.name = name
    
    @classmethod
    def from_description(cls, desc):
        # Create an instance using the description
        return cls(desc.upper())
    
    def describe(self):
        return f"This is a shape named {self.name}"

class Circle(Shape):
    def __init__(self, name):
        super().__init__(name)
    
    def describe(self):
        return f"A circle named {self.name}"

# Example usage
shape = Shape.from_description("hexagon")
circle = Circle.from_description("donut")
# - Shape.from_description("hexagon") → creates an instance of Shape with name "HEXAGON"
# - Circle.from_description("donut") → creates an instance of Circle with name "DONUT" because cls refers to Circle here!

# 8. 📚 Special Methods (Magic/Dunder Methods)
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"{self.title} by {self.author}"

book = Book("1984", "George Orwell")
print(book)  # Output: 1984 by George Orwell

# 9. 💡 Benefits of OOP
# - Reusability of code via inheritance.
# - Encapsulation hides complexity.
# - Clear modular structure of programs.
# - Easier debugging and maintenance.

# 10. 🧪 Practice Exercise
# OOP Challenge: Vehicle Management System
# Create a small object-oriented system for managing different types of vehicles.

# 🔧 Requirements:
# 1. Base Class: Vehicle
#    - Attributes: make, model, year, _mileage (protected)
#    - Methods:
#      - drive(distance) → increases _mileage
#      - get_info() → returns string summary
#      - __str__() → readable string representation
#    - Use encapsulation to protect _mileage.

# 2. Subclass: Car
#    - Additional attribute: fuel_capacity
#    - Overrides get_info() to include fuel capacity.
#    - Class-level attribute: vehicle_type = "Car"

# 3. Subclass: ElectricScooter
#    - Additional attribute: battery_percentage
#    - Overrides drive(distance) to reduce battery percentage.
#    - Add a static method is_charging_required() that returns True if battery < 20%.

# 4. Class Method:
#    - In Vehicle, add a class method from_string() that takes a string like "Toyota-Corolla-2020" and returns a Vehicle instance.

# 5. Polymorphism:
#    - Write a function print_vehicle_report(vehicles) that takes a list of vehicles and calls get_info() on each — regardless of its class.

# Sample Implementation
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self._mileage = 0
    
    def drive(self, distance):
        if distance > 0:
            self._mileage += distance
    
    def get_info(self):
        return f"{self.year} {self.make} {self.model}, Mileage: {self._mileage}"
    
    def __str__(self):
        return self.get_info()
    
    @classmethod
    def from_string(cls, string):
        make, model, year = string.split('-')
        return cls(make, model, int(year))

class Car(Vehicle):
    vehicle_type = "Car"
    
    def __init__(self, make, model, year, fuel_capacity):
        super().__init__(make, model, year)
        self.fuel_capacity = fuel_capacity
    
    def get_info(self):
        return f"{super().get_info()}, Fuel Capacity: {self.fuel_capacity}"

class ElectricScooter(Vehicle):
    def __init__(self, make, model, year, battery_percentage):
        super().__init__(make, model, year)
        self.battery_percentage = battery_percentage
    
    def drive(self, distance):
        super().drive(distance)
        self.battery_percentage -= distance * 0.1
        if self.battery_percentage < 0:
            self.battery_percentage = 0
    
    def get_info(self):
        return f"{super().get_info()}, Battery: {self.battery_percentage}%"
    
    @staticmethod
    def is_charging_required():
        return self.battery_percentage < 20

def print_vehicle_report(vehicles):
    for vehicle in vehicles:
        print(vehicle.get_info())

# Sample Output
vehicles = [
    Car("Toyota", "Corolla", 2020, 50),
    ElectricScooter("Xiaomi", "M365", 2022, 85),
    Vehicle.from_string("Honda-Civic-2018")
]
for v in vehicles:
    v.drive(100)
print_vehicle_report(vehicles)