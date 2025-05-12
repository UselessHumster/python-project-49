from random import randint

from brain_games.games.core import ask
from brain_games.games.utils import (
    END_RANDOM,
    NO_ANSWER,
    START_RANDOM,
    YES_ANSWER,
    is_answer_correct,
    print_wrong_answer,
)

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_correct_answer(number: int):
    if number % 2 == 0:
        return YES_ANSWER
    return NO_ANSWER


def game():
    number = randint(START_RANDOM, END_RANDOM)
    correct_answer = get_correct_answer(number)

    question = (f'Question: {number}\n'
                f'Your answer: ')
    user_answer = ask(question)

    if is_answer_correct(str(user_answer), str(correct_answer)):
        return True

    print_wrong_answer(user_answer, correct_answer)
    return False