from brain_games.games import CALC_RULE, calc_game, start_game


def main():
    start_game(calc_game, CALC_RULE)


if __name__ == '__main__':
    main()