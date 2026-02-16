"""
Eric Su Huang
Groupe 1234
Jeu Roche Papier Ciseaux avec interface graphique Arcade.
"""

import arcade
import random
from enum import Enum
from Game_state import GameState
from Attack_animation import AttackAnimation
from Attack_animation import AttackType

LARGEUR_ECRAN = 1200
HAUTEUR_ECRAN = 800
TITRE_ECRAN = "Roche Papier Ciseaux"


# Énumération des choix
class Choix(Enum):
    """
    Énumération des choix possibles dans le jeu Roche Papier Ciseaux.
    Attributs:
        ROCHE: Choix "roche" qui bat "ciseaux"
        PAPIER: Choix "papier" qui bat "roche"
        CISEAUX: Choix "ciseaux" qui bat "papier"
    """
    ROCHE = "roche"
    PAPIER = "papier"
    CISEAUX = "ciseaux"


# Variables globales de l'état du jeu
choix_joueur = ""  # Le choix actuel du joueur (roche, papier ou ciseaux)
choix_ordinateur = ""  # Le choix aléatoire de l'ordinateur
resultat_jeu = "Choisissez roche, papier ou ciseaux (R/P/C)"  # Message affichant le résultat de la dernière manche


# Classe principale du jeu
class MyGame(arcade.Window):
    """
    Classe principale gérant la fenêtre et la logique du jeu Roche Papier Ciseaux.
    """

    def __init__(self, width, height, title):
        """
        Initialise la fenêtre de jeu.
        """
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.victoires_joueur = 0  # Nombre de victoires remportées par le joueur.
        self.victoires_ordinateur = 0  # Nombre de victoires remportées par l'ordinateur.
        self.game_state = GameState.NOT_STARTED
        self.player_score = 0
        self.computer_score = 0
        self.player_attack_type = None
        self.computer_attack_type = None
        self.attack_selected = False

        self.roche = AttackAnimation(AttackType.ROCHE)
        self.papier = AttackAnimation(AttackType.PAPIER)

    def on_draw(self):
        """
        Dessine tous les éléments de l'interface graphique.
        """
        self.clear()

        # Titre du jeu
        arcade.draw_text(
            "Roche Papier Ciseaux",
            LARGEUR_ECRAN / 2,
            HAUTEUR_ECRAN - 50,
            arcade.color.BLACK,
            24,
            anchor_x="center",
        )

        # Affichage des scores
        arcade.draw_text(
            f"Victoires Joueur : {self.victoires_joueur} | Victoires Ordinateur : {self.victoires_ordinateur}",
            LARGEUR_ECRAN / 2,
            HAUTEUR_ECRAN - 20,
            arcade.color.BLACK,
            14,
            anchor_x="center",
        )

        # Affichage du choix du joueur (en bleu)
        arcade.draw_text(
            f"Votre choix : {choix_joueur}",
            LARGEUR_ECRAN / 4,
            HAUTEUR_ECRAN / 2,
            arcade.color.BLUE,
            16,
            anchor_x="center",
        )

        # Affichage du choix de l'ordinateur (en rouge)
        arcade.draw_text(
            f"Choix de l'ordinateur : {choix_ordinateur}",
            3 * LARGEUR_ECRAN / 4,
            HAUTEUR_ECRAN / 2,
            arcade.color.RED,
            16,
            anchor_x="center",
        )

        # Affichage du résultat de la manche
        arcade.draw_text(
            resultat_jeu,
            LARGEUR_ECRAN / 2,
            HAUTEUR_ECRAN / 2 - 50,
            arcade.color.BLACK,
            18,
            anchor_x="center",
        )

        # Instructions de jeu
        arcade.draw_text(
            "Appuyez sur R pour Roche, P pour Papier, C pour Ciseaux",
            LARGEUR_ECRAN / 2,
            50,
            arcade.color.GRAY,
            12,
            anchor_x="center",
        )


    def on_key_press(self, key, modifiers):
        """
        Traite les entrées clavier du joueur.
        """
        global choix_joueur, choix_ordinateur, resultat_jeu

        # Changement d'état
        if key == arcade.key.R:
            choix_joueur = "roche"
        elif key == arcade.key.P:
            choix_joueur = "papier"
        elif key == arcade.key.C:
            choix_joueur = "ciseaux"
        else:
            return  # Ignorer les autres clés

        # Sélection aléatoire du choix de l'ordinateur parmi l'énumération
        choix_ordinateur = random.choice([c.value for c in Choix])

        # Détermination et affichage du résultat
        resultat_jeu = self.determiner_gagnant(choix_joueur, choix_ordinateur)

    def determiner_gagnant(self, joueur, ordinateur):
        """
        Détermine le gagnant de la manche et met à jour les scores.
        """
        # Cas d'égalité
        if joueur == ordinateur:
            return "Égalité !"

        # Cas où le joueur gagne
        elif (joueur == "roche" and ordinateur == "ciseaux") or \
                (joueur == "papier" and ordinateur == "roche") or \
                (joueur == "ciseaux" and ordinateur == "papier"):
            self.victoires_joueur += 1
            return f"{joueur.capitalize()} bat {ordinateur} ! Vous gagnez !"

        # Cas où l'ordinateur gagne
        else:
            self.victoires_ordinateur += 1
            return f"{ordinateur.capitalize()} bat {joueur} ! Vous perdez."


def main():
    """
    Fonction principale qui initialise et lance le jeu.
    """
    MyGame(LARGEUR_ECRAN, HAUTEUR_ECRAN, TITRE_ECRAN)
    arcade.run()


# Point d'entrée du programme
if __name__ == "__main__":
    main()
