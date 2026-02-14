import arcade
import os




class VEICOLI():


    def __init__(self, Movimento, ):
        self.velocita = None
        self.velocita_angle : int| float = 1
        self.sprite = None
        self.change_x : int | float = 0
        self.change_y : int | float = 0
        self.change_angle : int | float = 0

    def Movimento(self):
        self.change_x += self.velocita
        self.change_y += self.velocita
        self.change_angle += self.velocita_angle


class Macchina1(VEICOLI):
    def super.__init__(self, Movimento)

    



