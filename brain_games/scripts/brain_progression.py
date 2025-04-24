from brain_games.games import (
    PROGRESSION_RULE,
    progression_game,
    start_game,
)

if __name__ == '__main__':
    start_game(progression_game, PROGRESSION_RULE)