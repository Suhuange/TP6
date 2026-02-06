"""
Fichier: attack_animation.py
Auteur: [Votre nom]
Description: Définit les types d'attaques et la classe d'animation pour les attaques.
"""


from enum import Enum
import arcade


class AttackType(Enum):
    """
    Énumération des différents types d'attaques possibles.
    """
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


class AttackAnimation(arcade.Sprite):
    """
    Classe représentant une animation d'attaque avec deux frames.
    Hérite de arcade.Sprite pour bénéficier des fonctionnalités de base.
    Attributs de classe:
    ATTACK_SCALE: Échelle de l'animation (0.5 = moitié moins gros)
    ANIMATION_SPEED: Vitesse de l'animation (secondes entre chaque frame)
    """


ATTACK_SCALE = 0.50
ANIMATION_SPEED = 0.2  # 200ms entre chaque changement d'image


def __init__(self, attack_type):
    """
    Initialise une animation d'attaque.
    Args:
    attack_type (AttackType): Le type d'attaque (ROCK, PAPER ou SCISSORS)
    """
    super().__init__()
    self.attack_type = attack_type
    self.texture_change_timer = 0.0
    # Charger les images appropriées selon le type d'attaque
    if self.attack_type == AttackType.ROCK:
        self.textures = [
        arcade.load_texture("assets/srock.png"),
        arcade.load_texture("assets/srock-attack.png"),
    ]

    elif self.attack_type == AttackType.PAPER:
        self.textures = [
        arcade.load_texture("assets/spaper.png"),
        arcade.load_texture("assets/spaper-attack.png"),
]

    else:  # SCISSORS
        self.textures = [
        arcade.load_texture("assets/scissors.png"),
        arcade.load_texture("assets/scissors-close.png"),
]

    self.scale = self.ATTACK_SCALE
    self.current_texture = 0
    self.set_texture(self.current_texture)


def on_update(self, delta_time: float = 1 / 60):
    """
    Met à jour l'animation en fonction du temps écoulé.
    Args:
    delta_time (float): Temps écoulé depuis la dernière mise à jour (en secondes)
    """

    # Accumuler le temps écoulé
    self.texture_change_timer += delta_time
    # Changer de texture si le temps d'animation est écoulé
    if self.texture_change_timer >= self.ANIMATION_SPEED:
        self.texture_change_timer = 0.0
        self.current_texture += 1

    if self.current_texture >= len(self.textures):
        self.current_texture = 0
        self.set_texture(self.current_texture)
