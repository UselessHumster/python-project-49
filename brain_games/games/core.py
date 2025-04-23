import prompt

from brain_games.games.config import GAMES_TO_WIN

def wrong_answer(user_answer, correct_answer):
    print(f"'{user_answer}' is wrong answer ;(. "
          f"Correct answer was '{correct_answer}'")


def ask(question: str):
    answer = prompt.string(question)
    return answer


def greetings(game_question:str):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game_question)
    return name

def start_game(game, game_question: str):
    name = greetings(game_question)


    won_games = 0
    while won_games < GAMES_TO_WIN:
        if game():
            won_games += 1

        else:
            break

    if won_games == GAMES_TO_WIN:
        print(f'Congratulations, {name}')