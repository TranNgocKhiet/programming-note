---
title: "06_Classes"
weight: 6
chapter: false
---

# Classes

## Syntax

Input
```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        self.is_running = True
        print("Car started.")
    
    def drive(self):
        if self.is_running:
            print("Car is moving.")
        else:
            print("Car is not started yet.")

my_car = Car("Toyota", "Corolla", 2022)
print('My car: ', my_car.make, my_car.model, my_car.year)
my_car.start()
my_car.drive()
```

Output
```
My car:  Toyota Corolla 2022
Car started.
Car is moving.
```

---

## Inheritance

Input
```python
class Animal:
    
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    
    def bark(self):
        print("Dog barks")
    
    def wag_tail(self):
        print("Dog wags tail")

dog = Dog()
dog.speak()
dog.bark()
```

Output
```
Animal speaks
Dog barks
```

---