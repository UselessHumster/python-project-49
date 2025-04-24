from brain_games.games import (
    PROGRESSION_RULE,
    progression_game,
    start_game,
)


def main():
    start_game(progression_game, PROGRESSION_RULE)


if __name__ == '__main__':
    main()