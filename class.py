# Clase Dog
class Dog:
    def __init__(self, size, color, race, price, name):
        self.size = size
        self.color = color
        self.race = race
        self.price = price
        self.name = name

    def walking(self):
        print(f"{self.name} is walking.")


Rufo = Dog("big", "blue", "Husky", 5000, "Rufo")
print(Rufo.size)
print(Rufo.color)
print(Rufo.race)
print(Rufo.price)
print(Rufo.name)
Rufo.walking()

DOC = Dog("big", "yellow with black", "Pastor Alemán", 1300000, "DOC")
print(DOC.size)
print(DOC.color)
print(DOC.race)
print(DOC.price)
print(DOC.name)

Mike = Dog("big", "white", "Pitbull", 500, "Mike")
print(Mike.size)
print(Mike.color)
print(Mike.race)
print(Mike.price)
print(Mike.name)

Kaiser = Dog("small", "white and brown", "Bulldog", 700, "Kaiser")
print(Kaiser.size)
print(Kaiser.color)
print(Kaiser.race)
print(Kaiser.price)
print(Kaiser.name)

Luna = Dog("small", "white and brown", "Labrador Retriever", 700, "Luna")
print(Luna.size)
print(Luna.color)
print(Luna.race)
print(Luna.price)
print(Luna.name)

# Clase Bird
class Bird:
    def __init__(self, size, color, species, price, name):
        self.size = size
        self.color = color
        self.species = species
        self.price = price
        self.name = name

    def flying(self):
        print(f"{self.name} is flying.")


Blue = Bird("small", "blue", "Parrot", 500, "Blue")
print(Blue.size)
print(Blue.color)
print(Blue.species)
print(Blue.price)
print(Blue.name)
Blue.flying()

Feather = Bird("small", "green", "Canary", 300, "Feather")
print(Feather.size)
print(Feather.color)
print(Feather.species)
print(Feather.price)
print(Feather.name)
Feather.flying()

Alba = Bird("small", "white", "Dove", 200, "Alba")
print(Alba.size)
print(Alba.color)
print(Alba.species)
print(Alba.price)
print(Alba.name)
Alba.flying()

Blu = Bird("small", "gray", "Sparrow", 150, "Blu")
print(Blu.size)
print(Blu.color)
print(Blu.species)
print(Blu.price)
print(Blu.name)
Blu.flying()

# Clase Cat
class Cat:
    def __init__(self, size, color, breed, price, name):
        self.size = size
        self.color = color
        self.breed = breed
        self.price = price
        self.name = name

    def meowing(self):
        print(f"{self.name} is meowing.")


Milo = Cat("small", "orange", "Persian", 800, "Milo")
print(Milo.size)
print(Milo.color)
print(Milo.breed)
print(Milo.price)
print(Milo.name)
Milo.meowing()

Lily = Cat("medium", "gray", "Russian Blue", 900, "Lily")
print(Lily.size)
print(Lily.color)
print(Lily.breed)
print(Lily.price)
print(Lily.name)
Lily.meowing()

Shadow = Cat("medium", "black", "Bombay", 1000, "Shadow")
print(Shadow.size)
print(Shadow.color)
print(Shadow.breed)
print(Shadow.price)
print(Shadow.name)
Shadow.meowing()

Snow = Cat("small", "white", "Angora", 750, "Snow")
print(Snow.size)
print(Snow.color)
print(Snow.breed)
print(Snow.price)
print(Snow.name)
Snow.meowing()
