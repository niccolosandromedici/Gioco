import arcade
import os
# from arcade import *

class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title, fullscreen=True)

        self.macchina = None
        self.playerSpriteList = arcade.SpriteList()
        

        self.setup()

    def on_draw(self):
        self.clear()
        self.playerSpriteList.draw()

   

    def setup(self):
        
        self.macchina = arcade.Sprite("./immagini/78614.png")

        self.macchina.center_x = 100
        self.macchina.center_y = 200
        self.macchina.scale_x = 1
        self.macchina.scale_y = 1
        self.macchina.angle = 0

        self.playerSpriteList.append(self.macchina)
        
        
        
        

    def on_draw(self):
        self.playerSpriteList.draw()
        
    def on_update(self, deltaTime):
        change_x = 0
        change_y = 0
        
        if self.up_pressed:
            change_y += self.velocita
        if self.down_pressed:
            change_y -= self.velocita
        if self.left_pressed:
            change_x -= self.velocita
        if self.right_pressed:
            change_x += self.velocita



    #def on_key_press(self, key, modifiers):
    #        if key == arcade.key.W:
    #           self.macchina.angle -= 10
    #        elif key == arcade.key.UP:
    #            self.macchina.angle -= 10
    #        elif key == arcade.key.A:
    #            self.macchina.center_x -= 10
    #        elif key == arcade.key.LEFT:
    #            self.macchina.center_x -= 10
    #        elif key == arcade.key.S:
    #            self.macchina.angle += 10
    #        elif key == arcade.key.DOWN:
    #            self.macchina.angle += 10
    #        elif key == arcade.key.D:
    #            self.macchina.center_x += 10
    #        elif key == arcade.key.RIGHT:
    #            self.macchina.center_x += 10



    def on_key_press(self, tasto, modificatori):
        if tasto in (arcade.key.UP, arcade.key.W):
            self.up_pressed = True
        elif tasto in (arcade.key.DOWN, arcade.key.S):
            self.down_pressed = True
        elif tasto in (arcade.key.LEFT, arcade.key.A):
            self.left_pressed = True
        elif tasto in (arcade.key.RIGHT, arcade.key.D):
            self.right_pressed = True




    def on_key_release(self, tasto, modificatori):
        """Gestisce il rilascio dei tasti"""
        if tasto in (arcade.key.UP, arcade.key.W):
            self.up_pressed = False
        elif tasto in (arcade.key.DOWN, arcade.key.S):
            self.down_pressed = False
        elif tasto in (arcade.key.LEFT, arcade.key.A):
            self.left_pressed = False
        elif tasto in (arcade.key.RIGHT, arcade.key.D):
            self.right_pressed = False






def main():
    game = MyGame(
        600, 600, "Il mio giochino"
    )
    arcade.run()



    
                                     


if __name__ == "__main__":
    main()

