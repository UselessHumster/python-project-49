from random import randint, choice

from brain_games.games.config import OPERATIONS

from brain_games.games.core import ask, wrong_answer, is_answer_correct


GAME_QUESTION = 'What is the result of the expression?'


def get_correct_answer(number1: int, number2: int, operation: str):
    if operation == '*':
        return number1 * number2

    elif operation == '-':
        return number1 - number2

    elif operation == '+':
        return number1 + number2


def game():
    number1 = randint(1, 10)
    number2 = randint(1, number1)
    operation = choice(OPERATIONS)
    correct_answer = get_correct_answer(number1, number2, operation)

    question = (f'{number1} {operation} {number2}\n'
                f'Your answer: ')
    user_answer = ask(question)

    if is_answer_correct(str(user_answer), str(correct_answer)):
        return True

    wrong_answer(user_answer, correct_answer)
    return False