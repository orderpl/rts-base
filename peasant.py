from pygame import Rect, Vector2, Surface
from peasantData import *

class Peasant(object):
    def __init__(self, pos:Vector2, size:Vector2, image:Surface, weight:float, height:float, profExp:PeasantProfession, milExp:PeasantMilitary):
        self.rect = Rect(pos, size)
        self.image = image
        
        self.weight = weight
        self.height = height
        self.strength = 2
        self.speed = 1
        
        self.food = 1
        self.alcohol = 0.1
        self.health = PeasantHealth(
            head=1,
            arms=1,
            legs=1,
            chest=1,
            stomache=1
        )
        
        self.happyness = 0
        
        self.professionExp = profExp
        self.militaryExp = milExp