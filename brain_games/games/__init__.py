from brain_games.games.core import start_game

from brain_games.games.brain_calc import game as calc_game
from brain_games.games.brain_calc import GAME_QUESTION as CALC_GAME_QUESTION

from brain_games.games.brain_even import game as even_game
from brain_games.games.brain_even import GAME_QUESTION as EVEN_GAME_QUESTION

__all__ = ['start_game',
           'calc_game', 'CALC_GAME_QUESTION',
           'even_game','EVEN_GAME_QUESTION']