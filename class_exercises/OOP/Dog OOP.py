#Dog Class Exercises


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name}, age: {self.age}'


class Dog(Animal):
#INHERITANCE
    species = "Canis familiaris"
    def description(self):
        return f"{self.name} is {self.age} years old"

    def bark(self):
        return "Woof!"

    def play(self, other):
        if isinstance(other, Dog):
            return f"{self.name} is playing with {other.name}!"
        elif isinstance(other, Animal):
            return f"{self.name} doesn't know how to play with {other.name}!"
        else:
            return f"{self.name} is not interested in playing with {other}!"

class Car:
    def __init__(self, colour, mileage):
        self.colour = colour
        self.mileage = mileage

    def __str__(self):
        return f"The {self.colour} car has {self.mileage} miles"