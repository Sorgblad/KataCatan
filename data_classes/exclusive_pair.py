from data_classes.player import Player


class Exclusive_Pair:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2

    def __eq__(self, other: 'Exclusive_Pair'):
        return {self.player1.get_player_number(), self.player2.get_player_number()} == {
            other.player1.get_player_number(), other.player2.get_player_number()}
