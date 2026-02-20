import arcade
from Attack_animation import AttackAnimation
from Attack_animation import AttackType


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(400, 200)
        arcade.set_background_color(arcade.color.BLACK)
        self.roche = AttackAnimation(AttackType.ROCHE)
        self.roche.position = 600, 400
        self.animation_update_time = 1.0 / AttackAnimation.ANIMATION_SPEED
        self.time_since_last_swap = 0.0

    def on_draw(self):
        self.roche.draw()

    def on_update(self, delta_time):
        self.roche.on_update()


MyGame(1200, 800, 'Window')
arcade.run()
