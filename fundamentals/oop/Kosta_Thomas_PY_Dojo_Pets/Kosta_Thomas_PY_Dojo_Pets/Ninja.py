from pet import Pet
from pet_cat import Cat


class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    def walk(self):
        self.pet.play()
        print(f"walking {self.pet.name}")
    def feed(self):
        self.pet.eat()
        print(f"Feeding {self.pet.name}")
    def bathe(self):
        self.pet.make_noise()
        print(f"You gave {self.pet.name} a bath, Ouch!")

my_cat = Cat("spot")
sneaky_ninja = Ninja("Dark", "Shadow", ["catnip", "fish bytes"],["dry food", "wet food"], my_cat)

sneaky_ninja.feed()
sneaky_ninja.walk()
sneaky_ninja.bathe()