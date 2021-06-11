class Dog:

    def __init__(self, name, colour):
        self.animal_kind = "canine"
        self.name = name
        self.colour = colour
        self.bark()

    def bark(self):
        print("woof")

Amy = Dog("Amy", "Golden")

print(Amy.name)
print(Amy.colour)