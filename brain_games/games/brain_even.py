from random import randint

from brain_games.games.config import YES, NO

from brain_games.games.core import ask


GAME_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'

def get_correct_answer(number: int):
    if number % 2 == 0:
        return YES
    return NO


def is_user_correct(number: int, answer: str):
    if answer == get_correct_answer(number):
        return True
    return False


def game():
    number = randint(1, 1000)
    correct_answer = get_correct_answer(number)

    question = f'Question: {number}\n'
    user_answer = ask(question)

    if is_user_correct(number, user_answer):
        return True

    print(f"'{user_answer}' is wrong answer ;(. "
          f"Correct answer was '{correct_answer}'")
    return False
