# next tasks: levelling up
# the more houses you knock at, the more knowledge you get
# the more times you get away, you get more points
# if you get caught, you lose

# the more people in your squad, the harder it is to get away. Also squad points?
# the house number should mean something...

from random import *
from player import *
from enemies import *

squad = int(input("How many people are you playing with? (up to 10) "))
risk = int(input("How risky are you from 1 to 10? "))
house = int(input("What house number do you choose? (up to __) "))

player = Players(squad, 0, 8, 2, risk)
print(player)

player.knock()

seconds_you_stay = player.risk_level + (10 - player.speed)

if seconds_you_stay < residents.open_door():
    print(f"You ran away after {seconds_you_stay}.")
    print("You got away!")
else:
    print(f"You ran away after {seconds_you_stay}.")
    print("You got caught! Better luck next time.")
