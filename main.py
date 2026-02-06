"""
Fichier: main.py
Auteur: [Votre nom]
Description: Jeu Roche, Papier, Ciseaux utilisant la bibliothèque Arcade.
             Le joueur affronte l'ordinateur dans une série de manches.
             Le premier à 3 victoires remporte la partie.
"""

import arcade
import random
from enum import Enum
from game_state import GameState
from attack_animation import AttackAnimation, AttackType


class MyGame(arcade.Window):
    """
    Classe principale du jeu Roche, Papier, Ciseaux.
    
    Hérite de arcade.Window pour créer une fenêtre de jeu.
    
    Attributs:
        SCREEN_WIDTH: Largeur de l'écran en pixels
        SCREEN_HEIGHT: Hauteur de l'écran en pixels
        SCREEN_TITLE: Titre de la fenêtre
        game_state: État actuel du jeu (GameState)
        player_score: Score du joueur
        computer_score: Score de l'ordinateur
        player_attack_type: Type d'attaque choisi par le joueur (AttackType)
        computer_attack_type: Type d'attaque choisi par l'ordinateur (AttackType)
        player_has_chosen: Booléen indiquant si le joueur a fait son choix
        round_winner: Gagnant de la manche ("Joueur", "Ordinateur" ou "Égalité")
        attack_sprites: Liste des sprites d'attaque disponibles
        computer_sprite: Sprite représentant l'attaque de l'ordinateur
        player_sprite: Sprite représentant l'attaque du joueur
    """
    
    SCREEN_WIDTH = 1024
    SCREEN_HEIGHT = 768
    SCREEN_TITLE = "Roche, Papier, Ciseaux"
    
    def __init__(self):
        """
        Initialise la fenêtre et les attributs du jeu.
        """
        super().__init__(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.SCREEN_TITLE)
        
        # État initial du jeu
        self.game_state = GameState.NOT_STARTED
        
        # Scores
        self.player_score = 0
        self.computer_score = 0
        
        # Attaques
        self.player_attack_type = None
        self.computer_attack_type = None
        self.player_has_chosen = False
        
        # Résultat de la manche
        self.round_winner = ""
        
        # Sprites
        self.attack_sprites = []
        self.computer_sprite = None
        self.player_sprite = None
        
        # Couleurs
        self.background_color = arcade.color.AMAZON
        
        # Initialisation des sprites
        self.setup()
    
    def setup(self):
        """
        Initialise les sprites et les éléments graphiques du jeu.
        """
        # Créer les sprites d'attaque pour la sélection du joueur
        self.attack_sprites = []
        
        # Position des sprites de sélection
        positions = [
            (self.SCREEN_WIDTH // 4, self.SCREEN_HEIGHT // 3),      # Roche à gauche
            (self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 3),      # Papier au centre
            (self.SCREEN_WIDTH * 3 // 4, self.SCREEN_HEIGHT // 3),  # Ciseaux à droite
        ]
        
        attack_types = [AttackType.ROCK, AttackType.PAPER, AttackType.SCISSORS]
        
        for i, (x, y) in enumerate(positions):
            sprite = AttackAnimation(attack_types[i])
            sprite.center_x = x
            sprite.center_y = y
            self.attack_sprites.append(sprite)
    
    def on_draw(self):
        """
        Dessine tous les éléments à l'écran en fonction de l'état du jeu.
        """
        arcade.start_render()
        
        # Dessiner l'arrière-plan
        arcade.set_background_color(self.background_color)
        
        # Afficher le titre
        arcade.draw_text(
            "ROCHE, PAPIER, CISEAUX",
            self.SCREEN_WIDTH // 2,
            self.SCREEN_HEIGHT - 100,
            arcade.color.WHITE,
            36,
            anchor_x="center",
            font_name="Arial"
        )
        
        # Afficher les scores
        arcade.draw_text(
            f"Joueur: {self.player_score}",
            100,
            self.SCREEN_HEIGHT - 150,
            arcade.color.WHITE,
            24,
            font_name="Arial"
        )
        
        arcade.draw_text(
            f"Ordinateur: {self.computer_score}",
            self.SCREEN_WIDTH - 200,
            self.SCREEN_HEIGHT - 150,
            arcade.color.WHITE,
            24,
            font_name="Arial"
        )
        
        # Afficher les instructions en fonction de l'état du jeu
        if self.game_state == GameState.NOT_STARTED:
            arcade.draw_text(
                "Appuyez sur ESPACE pour commencer",
                self.SCREEN_WIDTH // 2,
                self.SCREEN_HEIGHT // 2,
                arcade.color.YELLOW,
                28,
                anchor_x="center",
                font_name="Arial"
            )
        
        elif self.game_state == GameState.ROUND_ACTIVE:
            arcade.draw_text(
                "Choisissez votre attaque avec la souris",
                self.SCREEN_WIDTH // 2,
                self.SCREEN_HEIGHT - 200,
                arcade.color.WHITE,
                24,
                anchor_x="center",
                font_name="Arial"
            )
            
            # Dessiner les étiquettes sous les sprites
            labels = ["ROCHE", "PAPIER", "CISEAUX"]
            for i, sprite in enumerate(self.attack_sprites):
                arcade.draw_text(
                    labels[i],
                    sprite.center_x,
                    sprite.center_y - 80,
                    arcade.color.WHITE,
                    20,
                    anchor_x="center",
                    font_name="Arial"
                )
            
            # Dessiner les sprites de sélection
            for sprite in self.attack_sprites:
                sprite.draw()
        
        elif self.game_state == GameState.ROUND_DONE:
            # Afficher les attaques choisies
            arcade.draw_text(
                "Vous avez choisi:",
                self.SCREEN_WIDTH // 4,
                self.SCREEN_HEIGHT // 2 + 100,
                arcade.color.WHITE,
                24,
                anchor_x="center",
                font_name="Arial"
            )
            
            if self.player_sprite:
                self.player_sprite.center_x = self.SCREEN_WIDTH // 4
                self.player_sprite.center_y = self.SCREEN_HEIGHT // 2
                self.player_sprite.draw()
            
            arcade.draw_text(
                "L'ordinateur a choisi:",
                self.SCREEN_WIDTH * 3 // 4,
                self.SCREEN_HEIGHT // 2 + 100,
                arcade.color.WHITE,
                24,
                anchor_x="center",
                font_name="Arial"
            )
            
            if self.computer_sprite:
                self.computer_sprite.center_x = self.SCREEN_WIDTH * 3 // 4
                self.computer_sprite.center_y = self.SCREEN_HEIGHT // 2
                self.computer_sprite.draw()
            
            # Afficher le résultat
            arcade.draw_text(
                self.round_winner,
                self.SCREEN_WIDTH // 2,
                self.SCREEN_HEIGHT // 2 - 100,
                arcade.color.YELLOW,
                32,
                anchor_x="center",
                font_name="Arial"
            )
            
            # Instructions pour continuer
            arcade.draw_text(
                "Appuyez sur ESPACE pour la prochaine manche",
                self.SCREEN_WIDTH // 2,
                100,
                arcade.color.WHITE,
                24,
                anchor_x="center",
                font_name="Arial"
            )
        
        elif self.game_state == GameState.GAME_OVER:
            # Déterminer le gagnant final
            winner = "Joueur" if self.player_score > self.computer_score else "Ordinateur"
            
            arcade.draw_text(
                f"{winner} a gagné la partie!",
                self.SCREEN_WIDTH // 2,
                self.SCREEN_HEIGHT // 2 + 50,
                arcade.color.GOLD,
                40,
                anchor_x="center",
                font_name="Arial"
            )
            
            arcade.draw_text(
                "Appuyez sur ESPACE pour recommencer",
                self.SCREEN_WIDTH // 2,
                self.SCREEN_HEIGHT // 2 - 50,
                arcade.color.WHITE,
                28,
                anchor_x="center",
                font_name="Arial"
            )
    
    def on_update(self, delta_time):
        """
        Met à jour la logique du jeu à chaque frame.
        
        Args:
            delta_time (float): Temps écoulé depuis la dernière mise à jour (en secondes)
        """
        # Mettre à jour les animations
        for sprite in self.attack_sprites:
            sprite.on_update(delta_time)
        
        if self.player_sprite:
            self.player_sprite.on_update(delta_time)
        
        if self.computer_sprite:
            self.computer_sprite.on_update(delta_time)
        
        # Logique de la manche active
        if (self.game_state == GameState.ROUND_ACTIVE and 
            self.player_has_chosen and 
            self.player_attack_type is not None):
            
            # Générer l'attaque de l'ordinateur
            computer_choice = random.randint(0, 2)
            
            if computer_choice == 0:
                self.computer_attack_type = AttackType.ROCK
            elif computer_choice == 1:
                self.computer_attack_type = AttackType.PAPER
            else:
                self.computer_attack_type = AttackType.SCISSORS
            
            # Créer les sprites d'attaque pour l'affichage
            self.player_sprite = AttackAnimation(self.player_attack_type)
            self.computer_sprite = AttackAnimation(self.computer_attack_type)
            
            # Déterminer le gagnant de la manche
            self.determine_round_winner()
            
            # Mettre à jour les scores
            if self.round_winner == "Joueur":
                self.player_score += 1
            elif self.round_winner == "Ordinateur":
                self.computer_score += 1
            
            # Vérifier si la partie est terminée
            if self.player_score >= 3 or self.computer_score >= 3:
                self.game_state = GameState.GAME_OVER
            else:
                self.game_state = GameState.ROUND_DONE
            
            # Réinitialiser le choix du joueur
            self.player_has_chosen = False
    
    def determine_round_winner(self):
        """
        Détermine le gagnant de la manche en fonction des attaques choisies.
        
        Règles:
            - Roche bat Ciseaux
            - Ciseaux bat Papier
            - Papier bat Roche
            - Égalité si les attaques sont identiques
        """
        if self.player_attack_type == self.computer_attack_type:
            self.round_winner = "Égalité!"
        
        elif self.player_attack_type == AttackType.ROCK:
            if self.computer_attack_type == AttackType.SCISSORS:
                self.round_winner = "Joueur gagne!"
            else:
                self.round_winner = "Ordinateur gagne!"
        
        elif self.player_attack_type == AttackType.PAPER:
            if self.computer_attack_type == AttackType.ROCK:
                self.round_winner = "Joueur gagne!"
            else:
                self.round_winner = "Ordinateur gagne!"
        
        elif self.player_attack_type == AttackType.SCISSORS:
            if self.computer_attack_type == AttackType.PAPER:
                self.round_winner = "Joueur gagne!"
            else:
                self.round_winner = "Ordinateur gagne!"
    
    def on_key_press(self, key, modifiers):
        """
        Gère les appuis sur les touches du clavier.
        
        Args:
            key (int): Code de la touche pressée
            modifiers (int): Modificateurs (Ctrl, Shift, etc.)
        """
        # Touche ESPACE pour gérer les transitions d'état
        if key == arcade.key.SPACE:
            if self.game_state == GameState.NOT_STARTED:
                self.game_state = GameState.ROUND_ACTIVE
            
            elif self.game_state == GameState.ROUND_DONE:
                self.game_state = GameState.ROUND_ACTIVE
                self.player_attack_type = None
                self.computer_attack_type = None
            
            elif self.game_state == GameState.GAME_OVER:
                # Réinitialiser le jeu
                self.player_score = 0
                self.computer_score = 0
                self.player_attack_type = None
                self.computer_attack_type = None
                self.player_has_chosen = False
                self.round_winner = ""
                self.player_sprite = None
                self.computer_sprite = None
                self.game_state = GameState.ROUND_ACTIVE
    
    def on_mouse_press(self, x, y, button, modifiers):
        """
        Gère les clics de souris pour sélectionner une attaque.
        
        Args:
            x (int): Coordonnée X du clic
            y (int): Coordonnée Y du clic
            button (int): Bouton de la souris pressé
            modifiers (int): Modificateurs (Ctrl, Shift, etc.)
        """
        # Ne traiter les clics que pendant une manche active
        if self.game_state != GameState.ROUND_ACTIVE:
            return
        
        # Vérifier si le joueur a cliqué sur un sprite d'attaque
        for i, sprite in enumerate(self.attack_sprites):
            if sprite.collides_with_point((x, y)):
                # Enregistrer le choix du joueur
                if i == 0:
                    self.player_attack_type = AttackType.ROCK
                elif i == 1:
                    self.player_attack_type = AttackType.PAPER
                else:
                    self.player_attack_type = AttackType.SCISSORS
                
                self.player_has_chosen = True
                break


def main():
    """
    Fonction principale pour lancer le jeu.
    """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
