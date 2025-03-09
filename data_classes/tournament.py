from typing import List

from data_classes.player import Player


class Tournament:
    def __init__(self, name : str, players : List[Player] = None ):
        self.name = name
        self.players = players