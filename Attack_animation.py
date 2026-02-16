"""
Eric Su
Groupe 1234
Gestion des types d'attaques et de leurs animations.
"""

import arcade
from enum import Enum


class AttackType(Enum):
    """Types possibles d'attaques."""
    ROCHE = 0
    PAPIER = 1
    CISEAUX = 2


class AttackAnimation(arcade.Sprite):
    """Sprite animé représentant une attaque."""

    ATTACK_SCALE = 0.5
    ANIMATION_SPEED = 5.0

    def __init__(self, attack_type):
        """Initialise l'animation selon le type d'attaque."""
        super().__init__()
        self.attack_type = attack_type

        if attack_type == AttackType.ROCHE:
            self.textures = [
                arcade.load_texture("sprites/IMG_0419.png"),
                arcade.load_texture("sprites/IMG_0420.png"),
            ]
        elif attack_type == AttackType.PAPIER:
            self.textures = [
                arcade.load_texture("sprites/IMG_0417.png"),
                arcade.load_texture("sprites/IMG_0418.png"),
            ]
        else:
            self.textures = [
                arcade.load_texture("sprites/IMG_0415.png"),
                arcade.load_texture("sprites/IMG_0416.png"),
            ]

        self.scale = self.ATTACK_SCALE
        self.current_texture = 0
        self.set_texture(self.current_texture)

        self.animation_update_time = 1.0 / self.ANIMATION_SPEED
        self.time_since_last_swap = 0.0

    def on_update(self, delta_time: float = 1 / 60):
        """Met à jour l'animation du sprite."""
        self.time_since_last_swap += delta_time
        if self.time_since_last_swap > self.animation_update_time:
            self.current_texture += 1
            if self.current_texture >= len(self.textures):
                self.current_texture = 0
            self.set_texture(self.current_texture)
            self.time_since_last_swap = 0.0
