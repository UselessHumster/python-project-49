from random import randint

import prompt

from .brain_games import GAMES_TO_WIN, NO, YES, welcome_user


def get_correct_answer(number):
    if number % 2 == 0:
        return YES
    return NO


def is_user_correct(number, answer):
    if answer == get_correct_answer(number):
        return True
    return False


def ask_is_even(number):
    answer = prompt.string(f'Question: {number}\n')
    return answer


def main():
    name = welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no".')

    won_games = 0
    while won_games < GAMES_TO_WIN:
        number = randint(1, 1000)
        correct_answer = get_correct_answer(number)
        user_answer = ask_is_even(number)

        if is_user_correct(number, user_answer):
            won_games += 1
            continue
        print(f"'{user_answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'")
        break

    if won_games == GAMES_TO_WIN:
        print(f'Congratulations, {name}')


if __name__ == '__main__':
    main()