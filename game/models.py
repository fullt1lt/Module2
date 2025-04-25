import random

def get_player_name():
    while True:
        name = input("Введите ваше имя:")
        if name:
            return name    


class Player:
    """Класс игрока"""
    
    def __init__(self):
        self.name = get_player_name()
        self.__score = 0
    
    def get_score(self):
        return self.__score
    
    def write_score(self, score):
        self.__score += score
        
    def move(self):
        while True:
            step = input("Нажмите Enter, чтобы бросить кубик...")
            if step:
                print("Неверный ввод. Нажмите Enter, чтобы бросить кубик.")
                continue
            return random.randint(1,6)
    
    
class Computer(Player):
    """Класс компьютера"""
    
    def __init__(self):
        self.name = "Computer"
        
    def move(self):
        return random.randint(1,6)