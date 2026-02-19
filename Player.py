import arcade
from Muri import Muri_

class Macchina(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.gravity : int | float = 1
        self.macchina_list = arcade.SpriteList()
        self.velocità : int | float | bool = None
        self.velocita_angle : int| float | bool = None

        
        self.physics_engine = arcade.PhysicsEnginePlatformer(self, walls = Muri_().wall_list, gravity_constant = self.gravity)
    
    def on_draw(self):
        self.macchina_list.draw()

    def on_update(self, delta_time: float):
        self.physics_engine.update()
        


class Macchina1(Macchina):
    def __init__(self):
        super().__init__()
        self.macchina1 = arcade.Sprite("./immagini/78614.png")
        self.macchina1.center_x : int = 100
        self.macchina1.center_y : int = 250
        self.macchina1.scale_x : int = 1
        self.macchina1.scale_y : int = 1
        self.macchina1.angle : int = 0
        self.velocita : int | float = 5
        self.macchina_list.append(self.macchina1)
    
    def on_update(self, delta_time):
        #movimento camera
        self.camera.position = self.macchina1.position



        