import pygame
from pygame import Surface, Vector2, Rect, draw

class Building(object):
    def __init__(self, game, image:Surface, rect:Rect) -> None:
        self.game = game
        self.image:Surface = image
        self.rect:Rect = rect
        
    def render(self):
        rendedRect = self.rect.copy()
        rendedRect.center += self.game.camera.pos
        draw.rect(self.game.screen, (255, 255, 255), rendedRect)