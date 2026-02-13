"""
Eric Su
Groupe 1234
Création d'un jeu de roche, papier, ciseaux avec la librairie Arcade
"""


from enum import Enum

class GameState(Enum):
    NOT_STARTED = 0
    ROUND_ACTIVE = 1
    ROUND_DONE = 2
    GAME_OVER = 3
