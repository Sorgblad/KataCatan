class Player:
    def __init__(self, name : str, surname : str, player_number : int, tournament_points : float, game_points : int, success_rate : float):
        self.name = name
        self.surname = surname
        self.player_number = player_number
        self.tournament_points = tournament_points
        self.game_points = game_points
        self.success_rate = success_rate