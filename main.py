```python
"""
Eric Su Huang
Groupe 1234
Jeu Roche Papier Ciseaux avec interface graphique Arcade.
"""

import arcade
import random
from enum import Enum
from Game_state import GameState
from Attack_animation import AttackAnimation, AttackType

# Constantes
LARGEUR_ECRAN = 1200
HAUTEUR_ECRAN = 800
TITRE_ECRAN = "Roche Papier Ciseaux"


# Énumération des choix
class Choix(Enum):
    ROCHE = "roche"
    PAPIER = "papier"
    CISEAUX = "ciseaux"


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.SEASHELL)

        # Scores
        self.victoires_joueur = 0
        self.victoires_ordinateur = 0

        # État du jeu
        self.game_state = GameState.NOT_STARTED

        # Variables du jeu (anciennement globales)
        self.choix_joueur = ""
        self.choix_ordinateur = ""
        self.resultat_jeu = "Choisissez roche, papier ou ciseaux"
        self.round_processed = False

        # Sprites (NE PAS MODIFIER)
        self.joueur = arcade.Sprite("sprites/IMG_0414.png", scale=0.7)
        self.ordinateur = arcade.Sprite("sprites/IMG_0413.png", scale=3.4)

        self.roche = AttackAnimation(AttackType.ROCHE)
        self.papier = AttackAnimation(AttackType.PAPIER)
        self.ciseaux = AttackAnimation(AttackType.CISEAUX)

        self.roche1 = AttackAnimation(AttackType.ROCHE)
        self.papier1 = AttackAnimation(AttackType.PAPIER)
        self.ciseaux1 = AttackAnimation(AttackType.CISEAUX)

        # Positions
        self.joueur.position = 300, 500
        self.ordinateur.position = 900, 500
        self.roche.position = 200, 200
        self.papier.position = 300, 200
        self.ciseaux.position = 400, 200
        self.roche1.position = 900, 200
        self.papier1.position = 900, 200
        self.ciseaux1.position = 900, 200

        # SpriteLists
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

    # ---------- MÉTHODES D’AFFICHAGE ----------
    def afficher_titre(self):
        arcade.draw_text(TITRE_ECRAN, LARGEUR_ECRAN / 2, HAUTEUR_ECRAN - 50,
                         arcade.color.BLACK, 24, anchor_x="center")

    def afficher_choix(self):
        arcade.draw_text(f"Votre choix : {self.choix_joueur}",
                         LARGEUR_ECRAN / 4, HAUTEUR_ECRAN / 3,
                         arcade.color.BLUE, 22, anchor_x="center")

        arcade.draw_text(f"Choix de l'ordinateur : {self.choix_ordinateur}",
                         3 * LARGEUR_ECRAN / 4, HAUTEUR_ECRAN / 3,
                         arcade.color.RED, 22, anchor_x="center")

    def afficher_message(self, texte):
        arcade.draw_text(texte, LARGEUR_ECRAN / 2, 700,
                         arcade.color.BLACK, 20, anchor_x="center")

    def afficher_resultat(self):
        arcade.draw_text(self.resultat_jeu,
                         LARGEUR_ECRAN / 2, HAUTEUR_ECRAN / 2 - 50,
                         arcade.color.BLACK, 18, anchor_x="center")

    def dessiner_cases(self):
        cases = [(161, 239), (261, 339), (361, 439), (861, 939)]
        for gauche, droite in cases:
            arcade.draw_lrbt_rectangle_outline(
                gauche, droite, 161, 239, arcade.color.DARK_GREEN
            )

    def afficher_scores(self):
        arcade.draw_text(
            f"Joueur : {self.victoires_joueur} | Ordi : {self.victoires_ordinateur}",
            LARGEUR_ECRAN / 2, HAUTEUR_ECRAN - 20,
            arcade.color.BLACK, 14, anchor_x="center"
        )

    def afficher_fin(self):
        self.afficher_message("PARTIE TERMINÉE! ESPACE pour rejouer")

        if self.victoires_joueur == 3:
            texte = "Vous avez gagné!"
            couleur = arcade.color.BLUE
        else:
            texte = "Vous avez perdu!"
            couleur = arcade.color.RED

        arcade.draw_text(texte, LARGEUR_ECRAN / 2, 650,
                         couleur, 30, anchor_x="center")

    # ---------- DRAW ----------
    def on_draw(self):
        self.clear()
        self.Sprites.draw()

        # Joueur
        if self.choix_joueur == "roche":
            self.attaque_roche.draw()
        elif self.choix_joueur == "papier":
            self.attaque_papier.draw()
        elif self.choix_joueur == "ciseaux":
            self.attaque_ciseaux.draw()

        # Ordi
        if self.choix_ordinateur == "roche":
            self.attaque_roche1.draw()
        elif self.choix_ordinateur == "papier":
            self.attaque_papier1.draw()
        elif self.choix_ordinateur == "ciseaux":
            self.attaque_ciseaux1.draw()

        self.afficher_titre()
        self.afficher_choix()

        if self.game_state == GameState.NOT_STARTED:
            self.afficher_message("Appuie sur ESPACE pour commencer")

        elif self.game_state == GameState.ROUND_ACTIVE:
            self.dessiner_cases()
            self.afficher_scores()
            self.afficher_message("Clique sur une attaque!")

            self.attaque_roche.draw()
            self.attaque_papier.draw()
            self.attaque_ciseaux.draw()

        elif self.game_state == GameState.ROUND_DONE:
            self.dessiner_cases()
            self.afficher_scores()
            self.afficher_resultat()
            self.afficher_message("Appuie sur ESPACE pour continuer")

        elif self.game_state == GameState.GAME_OVER:
            self.dessiner_cases()
            self.afficher_scores()
            self.afficher_resultat()
            self.afficher_fin()

    # ---------- UPDATE ----------
    def on_update(self, delta_time: float):

        # Animations
        self.roche.on_update(delta_time)
        self.roche1.on_update(delta_time)
        self.papier.on_update(delta_time)
        self.papier1.on_update(delta_time)
        self.ciseaux.on_update(delta_time)
        self.ciseaux1.on_update(delta_time)

        # LOGIQUE DU JEU (déplacée ici)
        if self.game_state == GameState.ROUND_ACTIVE \
           and self.choix_joueur != "" \
           and not self.round_processed:

            self.choix_ordinateur = random.choice([c.value for c in Choix])
            self.resultat_jeu = self.determiner_gagnant(
                self.choix_joueur, self.choix_ordinateur
            )

            if self.victoires_joueur >= 3 or self.victoires_ordinateur >= 3:
                self.game_state = GameState.GAME_OVER
            else:
                self.game_state = GameState.ROUND_DONE

            self.round_processed = True

    # ---------- INPUT ----------
    def on_mouse_press(self, x, y, button, modifiers):

        if self.game_state != GameState.ROUND_ACTIVE:
            return

        if self.roche.collides_with_point((x, y)):
            self.choix_joueur = "roche"
        elif self.papier.collides_with_point((x, y)):
            self.choix_joueur = "papier"
        elif self.ciseaux.collides_with_point((x, y)):
            self.choix_joueur = "ciseaux"
        else:
            return

        self.round_processed = False

    def on_key_press(self, key, modifiers):

        if key == arcade.key.SPACE:

            if self.game_state == GameState.NOT_STARTED:
                self.game_state = GameState.ROUND_ACTIVE

            elif self.game_state == GameState.ROUND_DONE:
                self.game_state = GameState.ROUND_ACTIVE
                self.choix_joueur = ""
                self.choix_ordinateur = ""
                self.round_processed = False

            elif self.game_state == GameState.GAME_OVER:
                self.game_state = GameState.ROUND_ACTIVE

                self.victoires_joueur = 0
                self.victoires_ordinateur = 0
                self.choix_joueur = ""
                self.choix_ordinateur = ""
                self.resultat_jeu = ""
                self.round_processed = False

    # ---------- LOGIQUE ----------
    def determiner_gagnant(self, joueur, ordinateur):

        if joueur == ordinateur:
            return "Égalité !"

        elif (joueur == "roche" and ordinateur == "ciseaux") or \
             (joueur == "papier" and ordinateur == "roche") or \
             (joueur == "ciseaux" and ordinateur == "papier"):

            self.victoires_joueur += 1
            return f"{joueur.capitalize()} bat {ordinateur} ! Vous gagnez !"

        else:
            self.victoires_ordinateur += 1
            return f"{ordinateur.capitalize()} bat {joueur} ! Vous perdez."


def main():
    MyGame(LARGEUR_ECRAN, HAUTEUR_ECRAN, TITRE_ECRAN)
    arcade.run()


if __name__ == "__main__":
    main()
```
