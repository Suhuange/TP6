"""
Eric Su
Groupe 1234
Définit les états de jeu possibles pour le jeu Roche, Papier, Ciseaux
"""


from enum import Enum

class GameState(Enum):
    """
    Énumération des états posibles du jeu
    """
    NOT_STARTED = 0 # État initial, le jeu n'a pas encore commencé
    ROUND_ACTIVE = 1 # Un match est en cours
    ROUND_DONE = 2 # Le match est terminée, affichage du résultat
    GAME_OVER = 3 # La partie est terminée
