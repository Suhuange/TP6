class MyGame(arcade.Window):
 
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

        if self.game_state == GameState.ROUND_DONE:
            self.player.draw()
            self.ordinateur.draw()

            player_attack = self._get_player_attack_sprite()
            computer_attack = self._get_computer_attack_sprite()

            if player_attack:
                player_attack.draw()
            if computer_attack:
                computer_attack.draw()
        else:
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
    def _get_player_attack_sprite(self):
        """Retourne le sprite correspondant au dernier choix du joueur."""
        if choix_joueur == "roche":
            return self.roche
        if choix_joueur == "papier":
            return self.papier
        if choix_joueur == "ciseaux":
            return self.ciseaux
        return None

    def _get_computer_attack_sprite(self):
        """Retourne le sprite correspondant au dernier choix de l'ordinateur."""
        if choix_ordinateur == "roche":
            return self.roche1
        if choix_ordinateur == "papier":
            return self.papier1
        if choix_ordinateur == "ciseaux":
            return self.ciseaux1
        return None

 
 def main():
     """
     Fonction principale qui initialise et lance le jeu.
     """
     MyGame(LARGEUR_ECRAN, HAUTEUR_ECRAN, TITRE_ECRAN)
     arcade.run()
 
 
 # Point d'entrée du programme
 if __name__ == "__main__":
     main()
 
