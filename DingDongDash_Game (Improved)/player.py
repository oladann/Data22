from random import *

class Squad:
    def __init__(self):
        # self.no_of_players = no_of_players
        print("Squad goals")


class Players(Squad):
    def __init__(self, squad=2, points=0, knowledge=5, speed=2, risk_level=5):
        super().__init__()
        self.squad = squad
        self.points = points
        self.knowledge = knowledge  # knowledge of the area/neighbourhood
        self.speed = speed  # how fast you can get away
        self.risk_level = risk_level  # how risky are you?

    def __str__(self):
        return f"(Player stats: points = {self.points}, squad = {self.squad}, knowledge = {self.knowledge}, speed = {self.speed}, risk level = {self.risk_level})"

    # def display_player(self):
    #     print(self.knowledge)
    #     print(self.speed)
    #     print(self.squad)
    #     print(self.risk_level)

    def knock(self):
        print("Knock knock... \n")

    # def risk_level(self):
    #     # inputted/chosen by player

    # def run_away(self):
    #     run_after_seconds =  # inputted/chosen by player
    #     return run_after_seconds
