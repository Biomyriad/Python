class Animal:
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness
    def feed(self):
        self.health += 10
        self.happiness += 10
    def display_info(self):
        print(f"Name: {self.name} Health: {self.health} Happiness: {self.happiness}")

class Lion(Animal):
    def __init__(self, name, age = 1, health = 100, happiness = 100):
        super().__init__(name, age, health, happiness)
    def feed(self):
        super().feed()
        return self
    def display_info(self):
        super().display_info()
        return self

class Tiger(Animal):
    def __init__(self, name, age = 1, health = 100, happiness = 100):
        super().__init__(name, age, health, happiness)
    def feed(self):
        super().feed()
        return self
    def display_info(self):
        super().display_info()
        return self

class Bear(Animal):
    def __init__(self, name, age = 1, health = 100, happiness = 100):
        super().__init__(name, age, health, happiness)
    def feed(self):
        super().feed()
        return self
    def display_info(self):
        super().display_info()
        return self

class Zoo:
    def __init__(self, name):
        self.animals = []
        self.zoo_name = name
    def add_animal(self, animal):
        self.animals.append(animal)
        return self
    def print_all_info(self):
        print(f"----- {self.zoo_name} -----")
        for animal in self.animals:
            animal.display_info()
        return self



my_zoo = Zoo("ZooTopia")

my_zoo.add_animal(Lion("leo"))
my_zoo.add_animal(Tiger("Tigger").feed())
my_zoo.add_animal(Bear("Poo"))

my_zoo.print_all_info()