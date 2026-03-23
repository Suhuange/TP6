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

# Constantes
LARGEUR_ECRAN = 1200
HAUTEUR_ECRAN = 800
TITRE_ECRAN = "Roche Papier Ciseaux"

# Variables globales de l'état du jeu
choix_joueur = ""  # Le choix actuel du joueur (roche, papier ou ciseaux)
choix_ordinateur = ""  # Le choix aléatoire de l'ordinateur
resultat_jeu = "Choisissez roche, papier ou ciseaux"  # Message affichant le résultat de la dernière manche


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


# Décoration pour les mains
def cases():
    coords = [(161, 239), (261, 339), (361, 439), (861, 939)]
    for left, right in coords:
        arcade.draw_lrbt_rectangle_outline(left, right, 161, 239, arcade.color.DARK_GREEN)


# Classe principale du jeu
class MyGame(arcade.Window):
    """
    Classe principale gérant la fenêtre et la logique du jeu Roche Papier Ciseaux.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.SEASHELL)

        # Scores
        self.victoires_joueur = 0  # Nombre de victoires remportées par le joueur.
        self.victoires_ordinateur = 0

        # État initiale
        self.game_state = GameState.NOT_STARTED
        self.joueur_attaque_type = None
        self.ordinateur_attaque_type = None
        self.attack_selected = False

        # Sprites pour le joueur et l'ordianteur
        self.joueur = arcade.Sprite("sprites/IMG_0414.png", scale=0.7)
        self.ordinateur = arcade.Sprite("sprites/IMG_0413.png", scale=3.4)

        # Sprites pour les attaques du joueur
        self.roche = AttackAnimation(AttackType.ROCHE)
        self.papier = AttackAnimation(AttackType.PAPIER)
        self.ciseaux = AttackAnimation(AttackType.CISEAUX)

        # Sprites pour les attaques de l'ordinateur
        self.roche1 = AttackAnimation(AttackType.ROCHE)
        self.papier1 = AttackAnimation(AttackType.PAPIER)
        self.ciseaux1 = AttackAnimation(AttackType.CISEAUX)

        # Positions des Sprites
        self.joueur.position = 300, 500
        self.ordinateur.position = 900, 500
        self.roche.position = 200, 200
        self.papier.position = 300, 200
        self.ciseaux.position = 400, 200
        self.roche1.position = 900, 200
        self.papier1.position = 900, 200
        self.ciseaux1.position = 900, 200

        # Liste de sprites pour le dessiner
        self.Sprites = arcade.SpriteList()
        self.Sprites.append(self.joueur)
        self.Sprites.append(self.ordinateur)

        self.attaque_roche = arcade.SpriteList()
        self.attaque_roche.append(self.roche)

        self.attaque_papier = arcade.SpriteList()
        self.attaque_papier.append(self.papier)

        self.attaque_ciseaux = arcade.SpriteList()
        self.attaque_ciseaux.append(self.ciseaux)

        self.attaque_roche1 = arcade.SpriteList()
        self.attaque_roche1.append(self.roche1)

        self.attaque_papier1 = arcade.SpriteList()
        self.attaque_papier1.append(self.papier1)

        self.attaque_ciseaux1 = arcade.SpriteList()
        self.attaque_ciseaux1.append(self.ciseaux1)

    def on_draw(self):
        """
        Dessine tous les éléments de l'interface graphique.
        """
        self.clear()

        # Dessiner les sprites
        self.Sprites.draw()

        # Décoration pour les mains

        # Montrer seulement le Sprite que le joueur a choisi
        if choix_joueur == "roche":
            self.attaque_roche.draw()
        elif choix_joueur == "papier":
            self.attaque_papier.draw()
        elif choix_joueur == "ciseaux":
            self.attaque_ciseaux.draw()
        else:
            pass

        # Montrer seulement le Sprite que l'ordinateur a choisi
        if choix_ordinateur == "roche":
            self.attaque_roche1.draw()
        elif choix_ordinateur == "papier":
            self.attaque_papier1.draw()
        elif choix_ordinateur == "ciseaux":
            self.attaque_ciseaux1.draw()
        else:
            pass

        # Titre du jeu
        arcade.draw_text(
            "Roche Papier Ciseaux",
            LARGEUR_ECRAN / 2,
            HAUTEUR_ECRAN - 50,
            arcade.color.BLACK,
            24,
            anchor_x="center",
        )

        # Affichage du choix du joueur (en bleu)
        arcade.draw_text(
            f"Votre choix : {choix_joueur}",
            LARGEUR_ECRAN / 4,
            HAUTEUR_ECRAN / 3,
            arcade.color.BLUE,
            22,
            anchor_x="center",
        )

        # Affichage du choix de l'ordinateur (en rouge)
        arcade.draw_text(
            f"Choix de l'ordinateur : {choix_ordinateur}",
            3 * LARGEUR_ECRAN / 4,
            HAUTEUR_ECRAN / 3,
            arcade.color.RED,
            22,
            anchor_x="center",
        )

        # Affichage du texte pour changer d'état
        if self.game_state == GameState.NOT_STARTED:
            arcade.draw_text(
                "Appuie sur ESPACE pour commencer",
                LARGEUR_ECRAN / 2,
                700,
                arcade.color.BLACK,
                20,
                anchor_x="center"
            )

        elif self.game_state == GameState.ROUND_ACTIVE:

            # Affichage des Sprites des attaques (roche, papier et ciseaux)
            self.attaque_roche.draw()
            self.attaque_papier.draw()
            self.attaque_ciseaux.draw()
            cases()
            # Affichage des scores
            arcade.draw_text(
                f"Victoires Joueur : {self.victoires_joueur} | Victoires Ordinateur : {self.victoires_ordinateur}",
                LARGEUR_ECRAN / 2,
                HAUTEUR_ECRAN - 20,
                arcade.color.BLACK,
                14,
                anchor_x="center",
            )

            arcade.draw_text(
                f"Appuyer sur une image pour faire une attaque!",
                LARGEUR_ECRAN / 2,
                HAUTEUR_ECRAN - 90,
                arcade.color.BLACK,
                20,
                anchor_x="center",
            )

        elif self.game_state == GameState.ROUND_DONE:

            # Décoration pour les mains
            arcade.draw_lrbt_rectangle_outline(161, 239, 161, 239, arcade.color.DARK_GREEN)
            arcade.draw_lrbt_rectangle_outline(261, 339, 161, 239, arcade.color.DARK_GREEN)
            arcade.draw_lrbt_rectangle_outline(361, 439, 161, 239, arcade.color.DARK_GREEN)
            arcade.draw_lrbt_rectangle_outline(861, 939, 161, 239, arcade.color.DARK_GREEN)

            # Affichage du résultat de la manche
            arcade.draw_text(
                resultat_jeu,
                LARGEUR_ECRAN / 2,
                HAUTEUR_ECRAN / 2 - 50,
                arcade.color.BLACK,
                18,
                anchor_x="center",
            )

            # Affichage du texte pour changer d'état
            arcade.draw_text(
                "Ronde terminée! Appuie sur ESPACE pour continuer",
                LARGEUR_ECRAN / 2,
                700,
                arcade.color.BLACK,
                20,
                anchor_x="center"
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

        else:

            # Décoration pour les mains
            arcade.draw_lrbt_rectangle_outline(161, 239, 161, 239, arcade.color.DARK_GREEN)
            arcade.draw_lrbt_rectangle_outline(261, 339, 161, 239, arcade.color.DARK_GREEN)
            arcade.draw_lrbt_rectangle_outline(361, 439, 161, 239, arcade.color.DARK_GREEN)
            arcade.draw_lrbt_rectangle_outline(861, 939, 161, 239, arcade.color.DARK_GREEN)

            # Affichage des scores
            arcade.draw_text(
                f"Victoires Joueur : {self.victoires_joueur} | Victoires Ordinateur : {self.victoires_ordinateur}",
                LARGEUR_ECRAN / 2,
                HAUTEUR_ECRAN - 20,
                arcade.color.BLACK,
                14,
                anchor_x="center",
            )

            # Affichage du texte pour changer d'état
            arcade.draw_text(
                "PARTIE TERMINÉE! Appuie sur ESPACE pour rejouer",
                LARGEUR_ECRAN / 2,
                700,
                arcade.color.BLACK,
                20,
                anchor_x="center"
            )

            if self.victoires_joueur == 3:
                arcade.draw_text(
                    "Vous êtes le gagnant!",
                    LARGEUR_ECRAN / 2,
                    650,
                    arcade.color.BLUE,
                    30,
                    anchor_x="center"
                )

            else:
                arcade.draw_text(
                    "Vous êtes le perdant!",
                    LARGEUR_ECRAN / 2,
                    650,
                    arcade.color.RED,
                    30,
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

        if self.roche.collides_with_point((x, y)):
            choix_joueur = "roche"
        elif self.papier.collides_with_point((x, y)):
            choix_joueur = "papier"
        elif self.ciseaux.collides_with_point((x, y)):
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
                self.game_state = GameState.ROUND_ACTIVE

                # réinitialiser les valeurs et recommencer une nouvelle partie
                self.victoires_joueur = 0
                self.victoires_ordinateur = 0
                choix_joueur = ""
                choix_ordinateur = ""
                resultat_jeu = ""

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
