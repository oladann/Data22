from random import *
from player import *
from enemies import *

squad = int(input("How many people are you playing with? (up to 10) "))
risk = int(input("How risky are you from 1 to 10? "))
house = int(input("What house number do you choose? (up to __) "))

player = Players(8, 2, squad, risk)
print(player)

player.knock()

if player.risk_level + (10 - player.speed) < residents.open_door():
    print(f"You ran away after {player.risk_level + (10 - player.speed)}.")
    print("You got away!")
else:
    print(f"You ran away after {player.risk_level + (10 - player.speed)}.")
    print("You got caught! Better luck next time.")

