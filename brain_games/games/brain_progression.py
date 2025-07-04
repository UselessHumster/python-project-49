from random import randint

from brain_games.games.core import ask
from brain_games.games.utils import (
    END_RANDOM,
    START_RANDOM,
    is_answer_correct,
    print_wrong_answer,
)

RULE = 'What number is missing in the progression?'
START_FOR_STEP = 1
END_FOR_STEP = 10

PROGRESSION_LENGTH_FROM = 5
PROGRESSION_LENGTH_TO = 10


def generate_progression():
    progression = []
    step = randint(START_FOR_STEP, END_FOR_STEP)
    num = randint(START_RANDOM, END_RANDOM)
    for i in range(randint(PROGRESSION_LENGTH_FROM, PROGRESSION_LENGTH_TO)):
        progression.append(str(num))
        num += step
    return progression


def get_correct_answer(progression):
    pull_number = randint(1, len(progression) - 1)
    return progression[pull_number]


def hide_correct_answer(progression: list, correct_answer):
    progression = progression.copy()
    progression[progression.index(correct_answer)] = '..'
    return progression


def game():
    progression = generate_progression()

    correct_answer = get_correct_answer(progression)

    hidden_progression = hide_correct_answer(progression, correct_answer)
    progression_to_show = " ".join(hidden_progression)
    question = (f'Question: {progression_to_show}\n'
                f'Your answer: ')
    user_answer = ask(question)

    if is_answer_correct(str(user_answer), str(correct_answer)):
        return True

    print_wrong_answer(user_answer, correct_answer)
    return False