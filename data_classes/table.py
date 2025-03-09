from typing import List

from data_classes.player import Player


class Table:
    def __init__(self, number : int, players : List[Player] = None ):
        self.number = number
        self.players = players