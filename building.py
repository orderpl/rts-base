import pygame
from pygame import Surface, Vector2, Rect, draw

class Building(object):
    def __init__(self, game, image:Surface, rect:Rect) -> None:
        self.game = game
        self.image:Surface = image
        self.rect:Rect = rect
        
    def render(self):
        rendedRect = Rect(self.game.camera.getOnScreenPos(Vector2(self.rect.topleft)), Vector2(self.rect.size) * self.game.camera.zoom)
        draw.rect(self.game.screen, (255, 255, 255), rendedRect)