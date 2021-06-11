from random import *

class Team:
    def __init__(self, no_of_players = 2):
        self.no_of_players = no_of_players




class Players:
    def __init__(self, knowledge=5, speed=2, squad=1, risk_level=5):
        self.knowledge = knowledge  # knowledge of the area/neighbourhood
        self.speed = speed  # how fast you can get away
        self.squad = squad  # how many people in your group playing
        self.risk_level = risk_level  # how risky are you?

    def __str__(self):
        return f"(Player stats: knowledge = {self.knowledge}, speed = {self.speed}, squad = {self.squad}, risk level = {self.risk_level})"

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
