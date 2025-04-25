from game.game import Game
from game.models import Player, Computer
from game.score import Score

def main():
    while True:
        print("\n1. Играть\n2. Посмотреть результаты\n3. Выйти")
        choice = input("Выберите действие: ")
        if choice == "1":
            player = Player()
            computer = Computer()
            game = Game(player, computer)
            game.start()
        elif choice == "2":
            score = Score()
            score.get_results()
        elif choice == "3":
            print("До встречи!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()