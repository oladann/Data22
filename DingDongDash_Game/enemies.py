#enemies = residents
from random import *
import time

class residents:
    def __init__(self, busy_ness, neighbourhood_score):
        self.busy_ness = busy_ness
        self.neighbourhood_score = neighbourhood_score

    def open_door():
        seconds = randint(1, 20)
        time.sleep(seconds/2)
        print(f"The door opens after {seconds} seconds...")
        return seconds