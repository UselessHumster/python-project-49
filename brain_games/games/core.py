import prompt

from brain_games import greetings
from brain_games.games.utils import GAMES_TO_WIN


def ask(question: str):
    answer = prompt.string(question)
    return answer


def start_game(game, game_rule: str):
    name = greetings(game_rule)

    won_games = 0
    while won_games < GAMES_TO_WIN:
        if game():
            won_games += 1
            print('Correct!')
            continue
        print(f"Let's try again, {name}!")
        return

    if won_games == GAMES_TO_WIN:
        print(f'Congratulations, {name}!')
