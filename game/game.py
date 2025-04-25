from game.models import Player, Computer
from game.score import Score
from game.settings import GAME_LEVELS, GAME_LEVELS_CONVERT

def get_level():
    while True:
        level = input("Выберите уровень (1 - Short, 2 - Medium, 3 - Long): ")
        if level in GAME_LEVELS:
            return GAME_LEVELS[level]
        print("Неверный уровень. Попробуйте снова.")


class Game:
    def __init__(self, player: Player, computer: Computer):
        self.player = player
        self.computer = computer
        self.level = 0
        self.level_name = ""
        self.score = Score()

    def set_level(self):
        self.level = get_level()
        self.level_name = GAME_LEVELS_CONVERT[self.level]

    def print_results(self, current_round, step_player, step_computer):
        print(f"Раунд {current_round} из {self.level}")
        print(f"{self.player.name} бросил: {step_player}\n{self.computer.name} бросил: {step_computer}")
        print(f"Разница: {step_player - step_computer} очка")
        print("-----------------------")

    def check_winner(self, current_round, step_player, step_computer):
        diff = step_player - step_computer
        if diff == 0:
            print(f"Раунд {current_round} — ничья!")
            return False
        else:
            self.print_results(current_round, step_player, step_computer)
            self.player.write_score(diff)
            return True

    def play_round(self, current_round):
        step_player = self.player.move()
        step_computer = self.computer.move()
        return self.check_winner(current_round, step_player, step_computer)

    def start(self):
        self.set_level()

        current_round = 1
        while current_round <= self.level:
            if self.play_round(current_round):
                current_round += 1
        self.score.save_result(self.player, self.level_name)
