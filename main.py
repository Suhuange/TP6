"""
main.py
Jeu Roche, Papier, Ciseaux avec Arcade.

Fichier principal qui gère la fenêtre, les états du jeu,
les entrées clavier/souris et la logique du jeu.
"""

import arcade
import random

from game_state import GameState
from attack_animation import AttackAnimation, AttackType

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Roche, Papier, Ciseaux"


class MyGame(arcade.Window):
    """
    Classe principale du jeu.
    Hérite de arcade.Window.
    """

    def __init__(self):
        """Initialise la fenêtre et les variables du jeu."""
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.ALMOND)

        self.game_state = GameState.NOT_STARTED

        self.player_score = 0
        self.computer_score = 0

        self.player_attack_type = None
        self.computer_attack_type = None
        self.attack_selected = False

        self.rock = AttackAnimation(AttackType.ROCK)
        self.paper = AttackAnimation(AttackType.PAPER)
        self.scissors = AttackAnimation(AttackType.SCISSORS)

        self.rock.center_x = 200
        self.paper.center_x = 400
        self.scissors.center_x = 600

        for sprite in [self.rock, self.paper, self.scissors]:
            sprite.center_y = 200

    def on_draw(self):
        """Dessine tous les éléments à l'écran selon l'état du jeu."""
        self.clear()

        arcade.draw_text(
            "Roche, Papier, Ciseaux",
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT - 50,
            arcade.color.BLACK,
            24,
            anchor_x="center"
        )

        arcade.draw_text(
            f"Joueur: {self.player_score}  Ordinateur: {self.computer_score}",
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT - 100,
            arcade.color.BLACK,
            16,
            anchor_x="center"
        )

        self.rock.draw()
        self.paper.draw()
        self.scissors.draw()

        if self.game_state == GameState.NOT_STARTED:
            arcade.draw_text(
                "Appuie sur ESPACE pour commencer",
                SCREEN_WIDTH / 2,
                400,
                arcade.color.BLACK,
                18,
                anchor_x="center"
            )

        elif self.game_state == GameState.ROUND_DONE:
            arcade.draw_text(
                "Ronde terminée! Appuie sur ESPACE pour continuer",
                SCREEN_WIDTH / 2,
                400,
                arcade.color.BLACK,
                18,
                anchor_x="center"
            )

        elif self.game_state == GameState.GAME_OVER:
            arcade.draw_text(
                "PARTIE TERMINÉE! Appuie sur ESPACE pour rejouer",
                SCREEN_WIDTH / 2,
                400,
                arcade.color.RED,
                18,
                anchor_x="center"
            )

    def on_update(self, delta_time):
        """Met à jour la logique du jeu et les animations."""
        self.rock.on_update(delta_time)
        self.paper.on_update(delta_time)
        self.scissors.on_update(delta_time)

        if self.game_state == GameState.ROUND_ACTIVE and self.attack_selected:
            self.computer_attack_type = AttackType(random.randint(0, 2))
            self.validate_round()
            self.attack_selected = False
            self.game_state = GameState.ROUND_DONE

            if self.player_score == 3 or self.computer_score == 3:
                self.game_state = GameState.GAME_OVER

    def validate_round(self):
        """Détermine le gagnant de la ronde et met à jour le pointage."""
        p = self.player_attack_type
        c = self.computer_attack_type

        if p == c:
            return
        elif (
            (p == AttackType.ROCK and c == AttackType.SCISSORS)
            or (p == AttackType.PAPER and c == AttackType.ROCK)
            or (p == AttackType.SCISSORS and c == AttackType.PAPER)
        ):
            self.player_score += 1
        else:
            self.computer_score += 1

    def on_mouse_press(self, x, y, button, modifiers):
        """Gère le choix d'attaque du joueur avec la souris."""
        if self.game_state != GameState.ROUND_ACTIVE:
            return

        if self.rock.collides_with_point((x, y)):
            self.player_attack_type = AttackType.ROCK
            self.attack_selected = True
        elif self.paper.collides_with_point((x, y)):
            self.player_attack_type = AttackType.PAPER
            self.attack_selected = True
        elif self.scissors.collides_with_point((x, y)):
            self.player_attack_type = AttackType.SCISSORS
            self.attack_selected = True

    def on_key_press(self, key, modifiers):
        """Gère les transitions d'état avec le clavier."""
        if key == arcade.key.SPACE:
            if self.game_state == GameState.NOT_STARTED:
                self.game_state = GameState.ROUND_ACTIVE
            elif self.game_state == GameState.ROUND_DONE:
                self.game_state = GameState.ROUND_ACTIVE
            elif self.game_state == GameState.GAME_OVER:
                self.player_score = 0
                self.computer_score = 0
                self.game_state = GameState.ROUND_ACTIVE


def main():
    """Point d'entrée du programme."""
    game = MyGame()
    arcade.run()


if __name__ == "__main__":
    main()
