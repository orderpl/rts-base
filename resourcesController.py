from mathLib import formatUICoord
from random import random


class ResourceController:
    def __init__(self, game) -> None:
        self.screen, self.font = game.screen, game.fontNormal
        
        self.citizenHappyness = 0
        self.newCitizen = 0.0
        self.citizens = []
        self.maxHousing = 0
        
    def update(self):
        self.newCitizen += self.citizenHappyness / 1024

        freeSpace = self.maxHousing - len(self.citizens)
        growth = int(self.newCitizen)
        
        if growth < -len(self.citizens):
            self.citizens.clear()
        elif growth < 0:
            for i in range(-growth):
                self.citizens.pop(0)
        elif growth > freeSpace:
            growth = freeSpace
            for i in range(growth):
                self.citizens.append("gui")
        self.newCitizen -= growth
                
    def renderUI(self):
        poptext = self.font.render(f"{len(self.citizens)}/{self.maxHousing}", True, (255, 255, 255))
        self.screen.blit(poptext, (10, 10))