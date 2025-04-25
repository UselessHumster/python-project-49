import prompt

from brain_games.games.config import GAMES_TO_WIN
from brain_games import greetings


def is_answer_correct(answer: str, correct_answer: str):
    return answer == correct_answer


def wrong_answer(user_answer, correct_answer):
    print(f"'{user_answer}' is wrong answer ;(. "
          f"Correct answer was '{correct_answer}'")


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

        else:
            print(f"Let's try again, {name}!")
            break

    if won_games == GAMES_TO_WIN:
        print(f'Congratulations, {name}!')
