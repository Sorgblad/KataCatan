from typing import List

from data_classes.player import Player
from data_classes.game import Game


class Tournament:
    def __init__(self, name : str, players : List[Player] = None, games : List[Game] = None ):
        self.name = name
        self.players = players

    def fill_games(self, games : List[Game]):
        self.games = games