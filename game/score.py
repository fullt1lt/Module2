import json
from datetime import datetime

from game.settings import FILE_NAME

class Score:

    def get_results(self):
        result = self._load_results()
        print("Результаты игр:")
        for game in result:
            print(f"Дата: {game['date']},\nИмя игрока: {game['name']},\nОчки: {game['score']},\nКоличество раундов: {game['level']}")
            print("-" * 30)

    def _load_results(self):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_result(self, player, level):
        result = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "name": player.name,
            "score": player.get_score(),
            "level": level
        }
        print("Результат игры:")
        print(
            f"Дата: {result['date']},\nИмя игрока: {result['name']},\nОчки: {result['score']},\nКоличество раундов: {result['level']}"
        )
        print("-" * 30)
        results = self._load_results()
        results.append(result)
        self._save_to_file(results)
        print("Результат сохранен.")

    def _save_to_file(self, result):
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(result, file, indent=4, ensure_ascii=False)
