from Animal import Animal

class Reptile(Animal):   #inheritance

    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self.tetrapod = None
        self.heart_chambers = [3, 4]
        self.amniotic_eggs = None

    def seek_heat(self):
        print("It's chilly outside, where is the sun at???")

    def hunt(self):
        print("Wait for it, wait for it.....POUNCE!!!")

    def use_venom(self):
        print("If I have it, I am going to use it")

    def attract_mate_through_scent(self):
        print("Time to thow on the eau de toilette")


jeremy_the_reptile = Reptile()

sue_the_animal =Animal()

#encapsulation - hide details from the user