from random import randint, choice

from brain_games.games.config import OPERATIONS

from brain_games.games.core import ask


GAME_QUESTION = 'What is the result of the expression?'


def get_correct_answer(number1: int, number2: int, operation: str):
    if operation == '*':
        return number1 * number2

    elif operation == '-':
        return number1 - number2

    elif operation == '+':
        return number1 + number2


def is_user_correct(number1: int, number2: int, operation: str, answer: str):
    if answer.isnumeric():
        if int(answer) == get_correct_answer(number1, number2, operation):
            return True
    return False


def game():
    number1 = randint(1, 10)
    number2 = randint(1, number1)
    operation = choice(OPERATIONS)
    correct_answer = get_correct_answer(number1, number2, operation)

    question = f'{number1} {operation} {number2}\n'
    user_answer = ask(question)

    if is_user_correct(number1, number2, operation, user_answer):
        return True

    print(f"'{user_answer}' is wrong answer ;(. "
          f"Correct answer was '{correct_answer}'")
    return False