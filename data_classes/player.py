class Player:
    def __init__(self, name : str, surname : str, player_number : int, family : str):
        self.name = name
        self.surname = surname
        self.player_number = player_number
        self.family = family
        self.tournament_points = 0.0
        self.game_points_total = 0
        self.success_rate = 0.0

    def get_name(self) -> str:
        return self.name

    def get_surname(self) -> str:
        return self.surname

    def get_player_number(self) -> int:
        return self.player_number

    def get_tournament_points(self) -> float:
        return self.tournament_points

    def get_game_points_total(self) -> float:
        return self.game_points_total

    def get_success_rate(self) -> float:
        return self.success_rate

    def update_tournament_points(self, value: float) -> None:
        self.tournament_points += value

    def update_game_points_total(self, value: float) -> None:
        self.game_points_total += value

    def calculate_success_rate(self, value: float) -> None:
        if value == 0.0:
            self.success_rate += value
        else:
            self.success_rate /= value


    def is_the_same_family(self, target_player: "Player") -> bool:
        if self.family is None or target_player.family is None:
            return False
        else:
            return self.family == target_player.family
