class Animal:

    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True
    def breathe(self):
        print("One breath in and one breath out")
    def eat(self):
        print("nom nom nom nom")
    def procreate(self):
        print("It's time to find a mate")
    def move(self):
        print("Onwards and upwards")

cat = Animal()
cat.breathe()
