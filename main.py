import random
import arcade
     	
# Constantes
LARGEUR_ECRAN = 600
HAUTEUR_ECRAN = 400
TITRE_ECRAN = "Pierre Feuille Ciseaux"
CHOIX = ["pierre", "feuille", "ciseaux"]
     	
# État du jeu
choix_joueur = ""
choix_ordinateur = ""
resultat_jeu = "Choisissez pierre, feuille ou ciseaux (R/P/S)"
    	
    	
class MyGame(arcade.Window):
  def __init__(self, width, height, title):
    super().__init__(width, height, title)
    arcade.set_background_color(arcade.color.WHITE)
    self.victoires_joueur = 0
    self.victoires_ordinateur = 0
    	
  def on_draw(self):
    """Affiche l'écran."""
    self.clear()
    arcade.draw_text(
    "Roche Papier Ciseaux",
    LARGEUR_ECRAN / 2,
    HAUTEUR_ECRAN - 50,
    arcade.color.BLACK,
    24,
    anchor_x="center",
    )
    
    arcade.draw_text(
    f"Victoires Joueur : {self.victoires_joueur} | Victoires Ordinateur : {self.victoires_ordinateur}",
    LARGEUR_ECRAN / 2,
    HAUTEUR_ECRAN - 20,
    arcade.color.BLACK,
    14,
    anchor_x="center",
    )
    	
    arcade.draw_text(
    f"Votre choix : {choix_joueur}",
    LARGEUR_ECRAN / 4,
    HAUTEUR_ECRAN / 2,
    arcade.color.BLUE,
    16,
    anchor_x="center",
    )
    
    arcade.draw_text(
    f"Choix de l'ordinateur : {choix_ordinateur}",
    3 * LARGEUR_ECRAN / 4,
    HAUTEUR_ECRAN / 2,
    arcade.color.RED,
    16,
    anchor_x="center",
    )
    	
    arcade.draw_text(
    resultat_jeu,
    LARGEUR_ECRAN / 2
    HAUTEUR_ECRAN / 2 - 50,
    arcade.color.BLACK,
    18,
    anchor_x="center",
    )
    	
    arcade.draw_text(
    "Appuyez sur R pour Pierre, P pour Feuille, S pour Ciseaux",
    LARGEUR_ECRAN / 2,
    50,
    arcade.color.GRAY,
    12,
    anchor_x="center",
    )
    	
  def on_key_press(self, key, modifiers):
    """Appelée lorsqu'une clés est pressée."""
    global choix_joueur, choix_ordinateur, resultat_jeu
    if key == arcade.key.R:	
    	choix_joueur = "pierre"
    elif key == arcade.key.P:
    	choix_joueur = "feuille"
    elif key == arcade.key.S:
      choix_joueur = "ciseaux"
    else:
    	return  # Ignorer les autres clés
    	
  choix_ordinateur = random.choice(CHOIX)
  resultat_jeu = self.determiner_gagnant(choix_joueur, choix_ordinateur)
    	
  def determiner_gagnant(self, joueur, ordinateur):
    """Détermine le gagnant de la manche."""
    if joueur == ordinateur:
       return "Égalité !"
    elif (joueur == "pierre" and ordinateur == "ciseaux") or \
    (joueur == "feuille" and ordinateur == "pierre") or \
    (joueur == "ciseaux" and ordinateur == "feuille"):
      self.victoires_joueur += 1
      return f"{joueur.capitalize()} bat {ordinateur} ! Vous gagnez !"
    else:
      self.victoires_ordinateur += 1
        return f"{ordinateur.capitalize()} bat {joueur} ! Vous perdez."


def main():
"""Méthode principale."""
MyGame(LARGEUR_ECRAN, HAUTEUR_ECRAN, TITRE_ECRAN)
arcade.run()


if __name__ == "__main__":
 main()
