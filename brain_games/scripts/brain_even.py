from random import randint

import prompt

from brain_games import welcome_user

YES = 'yes'
NO = 'no'
GAMES_TO_WIN = 3


def get_correct_answer(number):
    if number % 2 == 0:
        return YES
    return NO


def check_answer(number, answer):
    if answer not in [YES, NO]:
        return False

    correct_answer = get_correct_answer(number)
    if answer == correct_answer:
        return True
    return False


def ask(number):
    answer = prompt.string(f'Question: {number}\n')
    return answer


def main():
    name = welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no".')

    won_games = 0
    while won_games < GAMES_TO_WIN:
        number = randint(1, 1000)
        correct_answer = get_correct_answer(number)
        user_answer = ask(number)
        is_answer_right = check_answer(number, user_answer)
        if is_answer_right:
            won_games += 1
            continue
        print(f"'{user_answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'")
        break

    if won_games == GAMES_TO_WIN:
        print(f'Congratulations, {name}')


if __name__ == '__main__':
    main()