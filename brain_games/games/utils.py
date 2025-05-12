YES_ANSWER = 'yes'
NO_ANSWER = 'no'

START_RANDOM = 1
END_RANDOM = 100

OPERATIONS = ['*', '-', '+']

GAMES_TO_WIN = 3


def is_answer_correct(answer: str, correct_answer: str):
    return answer == correct_answer


def print_wrong_answer(user_answer, correct_answer):
    print(
        f"'{user_answer}' is wrong answer ;(. "
        f"Correct answer was '{correct_answer}'")