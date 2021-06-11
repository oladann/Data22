class Dog:

    animal_kind = "Dolphin" # class variable which returns an attribute string

    def bark(self): # method
        return "woof"


Myles = Dog()
Oscar = Dog()

print(type(Myles))
print(type(Oscar))


Oscar.animal_kind = "Big Dog"
print(Myles.animal_kind)
print(Oscar.animal_kind)
print(Myles.bark())
print(Oscar.bark())

