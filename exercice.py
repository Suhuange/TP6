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
resultat_jeu = "Choisissez roche, papier ou ciseaux"  # Message affichant le résultat de la dernière manche


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

        self.player = arcade.Sprite("sprites/IMG_0414.png", scale=0.5)
        self.ordinateur = arcade.Sprite("sprites/IMG_0413.png", scale=2.5)
        self.roche = AttackAnimation(AttackType.ROCHE)
        self.papier = AttackAnimation(AttackType.PAPIER)
        self.ciseaux = AttackAnimation(AttackType.CISEAUX)
        self.roche1 = AttackAnimation(AttackType.ROCHE,)
        self.papier1 = AttackAnimation(AttackType.PAPIER)
        self.ciseaux1 = AttackAnimation(AttackType.CISEAUX)

        self.player.position = 300, 450
        self.ordinateur.position = 900, 450
        self.roche.position = 200, 200
        self.papier.position = 300, 200
        self.ciseaux.position = 400, 200
        self.roche1.position = 800, 200
        self.papier1.position = 900, 200
        self.ciseaux1.position = 1000, 200

        self.attacks_list = arcade.SpriteList()
        self.attacks_list.append(self.player)
        self.attacks_list.append(self.ordinateur)
        self.attacks_list.append(self.roche)
        self.attacks_list.append(self.papier)
        self.attacks_list.append(self.ciseaux)
        self.attacks_list.append(self.roche1)
        self.attacks_list.append(self.papier1)
        self.attacks_list.append(self.ciseaux1)

    def on_draw(self):
        """
        Dessine tous les éléments de l'interface graphique.
        """
        self.clear()
        self.attacks_list.draw()

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
            HAUTEUR_ECRAN / 3,
            arcade.color.BLUE,
            16,
            anchor_x="center",
        )

        # Affichage du choix de l'ordinateur (en rouge)
        arcade.draw_text(
            f"Choix de l'ordinateur : {choix_ordinateur}",
            3 * LARGEUR_ECRAN / 4,
            HAUTEUR_ECRAN / 3,
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
        if self.game_state == GameState.NOT_STARTED:
            arcade.draw_text(
                "Appuie sur ESPACE pour commencer",
                LARGEUR_ECRAN / 2,
                400,
                arcade.color.BLACK,
                18,
                anchor_x="center"
            )

        elif self.game_state == GameState.ROUND_DONE:
            arcade.draw_text(
                "Ronde terminée! Appuie sur ESPACE pour continuer",
                LARGEUR_ECRAN / 2,
                400,
                arcade.color.BLACK,
                18,
                anchor_x="center"
            )

        elif self.game_state == GameState.GAME_OVER:
            arcade.draw_text(
                "PARTIE TERMINÉE! Appuie sur ESPACE pour rejouer",
                LARGEUR_ECRAN / 2,
                400,
                arcade.color.RED,
                18,
                anchor_x="center"
            )

    def on_update(self, delta_time: float):
        """Met à jour la logique du jeu et les animations."""

        self.roche.on_update(delta_time)
        self.roche1.on_update(delta_time)
        self.papier.on_update(delta_time)
        self.papier1.on_update(delta_time)
        self.ciseaux.on_update(delta_time)
        self.ciseaux1.on_update(delta_time)

    def on_mouse_press(self, x, y, button, modifiers):
        """Gère le choix d'attaque du joueur avec la souris."""

        global choix_joueur, choix_ordinateur, resultat_jeu

        if self.game_state != GameState.ROUND_ACTIVE:
            return

        if self.roche.collides_with_point((200, 200)):
            choix_joueur = "roche"
        elif self.papier.collides_with_point((300, 200)):
            choix_joueur = "papier"
        elif self.ciseaux.collides_with_point((400, 200)):
            choix_joueur = "ciseaux"
        else:
            return

        # Sélection aléatoire du choix de l'ordinateur parmi l'énumération
        choix_ordinateur = random.choice([c.value for c in Choix])

        # Détermination et affichage du résultat
        resultat_jeu = self.determiner_gagnant(choix_joueur, choix_ordinateur)

        # Manche terminée
        if self.victoires_joueur >= 3 or self.victoires_ordinateur >= 3:
            self.game_state = GameState.GAME_OVER
        else:
            self.game_state = GameState.ROUND_DONE

    def on_key_press(self, key, modifiers):
        """Gère les transitions d'état avec le clavier."""
        global choix_joueur, choix_ordinateur, resultat_jeu

        if key == arcade.key.SPACE:

            if self.game_state == GameState.NOT_STARTED:
                self.game_state = GameState.ROUND_ACTIVE

            elif self.game_state == GameState.ROUND_DONE:
                self.game_state = GameState.ROUND_ACTIVE

            elif self.game_state == GameState.GAME_OVER:
                # réinitialiser les valeurs et recommencer une nouvelle partie
                self.victoires_joueur = 0
                self.victoires_ordinateur = 0
                choix_joueur = ""
                choix_ordinateur = ""
                resultat_jeu = ""
                self.game_state = GameState.ROUND_ACTIVE

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
