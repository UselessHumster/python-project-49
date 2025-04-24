from brain_games.games.core import start_game

from brain_games.games.brain_calc import game as calc_game
from brain_games.games.brain_calc import RULE as CALC_RULE

from brain_games.games.brain_even import game as even_game
from brain_games.games.brain_even import RULE as EVEN_RULE

from brain_games.games.brain_gcd import game as gcd_game
from brain_games.games.brain_gcd import RULE as GDC_RULE

from brain_games.games.brain_progression import game as progression_game
from brain_games.games.brain_progression import RULE as PROGRESSION_RULE

from brain_games.games.brain_prime import game as prime_game
from brain_games.games.brain_prime import RULE as PRIME_RULE


__all__ = ['start_game',
           'calc_game', 'CALC_RULE',
           'even_game','EVEN_RULE',
           'gcd_game','GDC_RULE',
           'progression_game','PROGRESSION_RULE',
           'prime_game', 'PRIME_RULE']