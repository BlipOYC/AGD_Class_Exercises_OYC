#Dog Class Exercises

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Name: {self.name}, age: {self.age}'

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, noise):
        return(f"{self.name} says {noise}")

class Cat(Animal):
    species = "Felis catus"

    def meow(self):
        return "Meow!"

    def play(self, other):
        if isinstance(other, Cat):
            return f"{self.name} is playing with {other.name}!"
        elif isinstance(other, Animal):
            return f"{self.name} doesn't know how to play with {other.__class__.__name__.lower()}s!"
        else:
            return f"{self.name} is not interested in playing with {other}!"

class Dog(Animal):
#INHERITANCE
    species = "Canis familiaris"


    def bark(self):
        return "Woof!"

    def play(self, other):
        if isinstance(other, Dog):
            return f"{self.name} is playing with {other.name}!"
        elif isinstance(other, Animal):
            return f"{self.name} doesn't know how to play with {other.__class__.__name__.lower()}s!"
        else:
            return f"{self.name} is not interested in playing with {other}!"

class Dachshund(Dog):
    def speak(self, noise="Arf! Arf!"):
        super().speak(noise)

class Car:
    def __init__(self, colour, mileage):
        self.colour = colour
        self.mileage = mileage

    def __str__(self):
        return f"The {self.colour} car has {self.mileage} miles"

taylor = Cat("Taylor", 4)
rufus = Dog("Rufus", 5)
fido = Dachshund("Fido", 4)