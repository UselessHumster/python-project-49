from random import choice, randint

from brain_games.games.core import ask
from brain_games.games.utils import (
    END_RANDOM,
    OPERATIONS,
    START_RANDOM,
    is_answer_correct,
    print_wrong_answer,
)

RULE = 'What is the result of the expression?'


def get_correct_answer(number1: int, number2: int, operation: str):
    if operation == '*':
        return number1 * number2

    elif operation == '-':
        return number1 - number2

    elif operation == '+':
        return number1 + number2


def game():
    number1 = randint(START_RANDOM, END_RANDOM)
    number2 = randint(START_RANDOM, number1)
    operation = choice(OPERATIONS)
    correct_answer = get_correct_answer(number1, number2, operation)

    question = (f'Question: {number1} {operation} {number2}\n'
                f'Your answer: ')
    user_answer = ask(question)

    if is_answer_correct(str(user_answer), str(correct_answer)):
        return True

    print_wrong_answer(user_answer, correct_answer)
    return False
