from itertools import combinations
from random import random
from typing import List

from data_classes.exclusive_pair import Exclusive_Pair
from data_classes.player import Player
from data_classes.game import Game


class Tournament:
    def __init__(self, name: str):
        self.games = List[Game]
        self.name = name
        self.players = List[Player]
        self.pairs = List[Exclusive_Pair]

    def fill_games(self, games: List[Game]):
        self.games = games

    def create_pairs(self):
        self.pairs = [Exclusive_Pair(p1,p2) for p1, p2 in combinations(self.players, 2)]

    def create_games(self):
        used_pairs = set()
        while len(used_pairs) < len(self.pairs):
            random.shuffle(self.pairs)