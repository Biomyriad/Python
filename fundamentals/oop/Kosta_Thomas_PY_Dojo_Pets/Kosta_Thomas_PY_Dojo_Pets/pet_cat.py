from pet import Pet

class Cat(Pet):
    def __init__(self, name):
        super().__init__(name,"cat", ["purr", "walk on KB"], "meow")
