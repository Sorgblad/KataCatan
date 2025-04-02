from typing import List, Mapping

from data_classes.player import Player


class Table:
    def __init__(self, number: int, players: List[Player] = None):
        self.number = number
        self.players = players
        self.result = {}

    def append_player(self, player: Player):
        self.players.append(player)

    def get_players(self) -> List[Player]:
        return self.players

    def get_number(self) -> int:
        return self.number

    def update_result(self, player: Player, result: int):
        if player in self.result: raise ValueError("Player is already mentioned.")
        self.result[player] = result

    def get_result(self, player: Player) -> int:
        return self.result[player]
