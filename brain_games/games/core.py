import prompt

from brain_games.games.config import GAMES_TO_WIN


def is_answer_correct(answer: str, correct_answer: str):
    return answer == correct_answer


def wrong_answer(user_answer, correct_answer):
    print(f"'{user_answer}' is wrong answer ;(. "
          f"Correct answer was '{correct_answer}'")


def ask(question: str):
    answer = prompt.string(question)
    return answer


def greetings(game_rule: str):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game_rule)
    return name


def start_game(game, game_question: str):
    name = greetings(game_question)

    won_games = 0
    while won_games < GAMES_TO_WIN:
        if game():
            won_games += 1
            print('Correct!')

        else:
            break

    if won_games == GAMES_TO_WIN:
        print(f'Congratulations, {name}')