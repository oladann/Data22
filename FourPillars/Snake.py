# Reptile inherits from Animal
# Snake inherits from Reptile

from Reptile import Reptile

class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.cold_blooded = True
        self.venom = None #Some states are venomous
        self.limbs = False

    def use_tongue_to_small(self):
        print("Do I smell nice, or do I taste nice?")

Oscar = Snake()
Oscar.seek_heat()
Oscar.use_tongue_to_small()

# this is encapsulation, because we are hiding how the seek.heat() method actually works bc its inherited
#from Reptile (encapulation is hiding functionality and attributes)