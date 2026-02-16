import arcade


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400, 200)
        arcade.set_background_color(arcade.color.BLACK)
        self.roche = arcade.Sprite("sprites/IMG_0419.png", scale=1, center_x=200, center_y=200)
        self.roche.position = 100, 200
        self.papier = arcade.Sprite("sprites/IMG_0417.png", scale=1, center_x=200, center_y=200)
        self.papier.position = 300, 200
        self.ciseaux = arcade.Sprite("sprites/IMG_0415.png", scale=1, center_x=200, center_y=200)
        self.ciseaux.position = 500, 200

        self.attacks_list = arcade.SpriteList()
        self.attacks_list.append(self.roche)
        self.attacks_list.append(self.papier)
        self.attacks_list.append(self.ciseaux)

    def on_draw(self):
        self.clear()
        self.attacks_list.draw()


MyGame(1200, 800, 'Window')
arcade.run()
