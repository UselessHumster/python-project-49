from random import randint

from brain_games.games.core import ask
from brain_games.games.utils import (
    END_RANDOM,
    START_RANDOM,
    is_answer_correct,
    print_wrong_answer,
)

RULE = 'Find the greatest common divisor of given numbers.'


def get_correct_answer(number1: int, number2: int):
    num1 = max(number1, number2)
    num2 = min(number1, number2)
    while True:
        remainder = num1 % num2
        if remainder == 0:
            return num2
        else:
            num1 = num2
            num2 = remainder


def game():
    number1 = randint(START_RANDOM, END_RANDOM)
    number2 = randint(START_RANDOM, END_RANDOM)
    correct_answer = get_correct_answer(number1, number2)

    question = (f'Question: {number1} {number2}\n'
                f'Your answer: ')
    user_answer = ask(question)

    if is_answer_correct(str(user_answer), str(correct_answer)):
        return True

    print_wrong_answer(user_answer, correct_answer)
    return False