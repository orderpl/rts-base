import pygame
from pygame import Surface, Vector2, Rect

class Building(object):
    def __init__(self, game, image:Surface, rect:Rect, imageOffset:Vector2) -> None:
        """Image offset is offset from center"""
        self.game = game
        self.imageOffset = imageOffset
        self.image:Surface = image
        self.imageRect:Rect = self.image.get_rect()
        self.rect:Rect = rect
        
    def render(self) -> None:
        renderRect = Rect(self.game.camera.getOnScreenPos(Vector2(self.rect.topleft)) + self.imageOffset, Vector2(self.rect.size) * self.game.camera.zoom)
        renderImage = pygame.transform.scale(self.image, Vector2(self.imageRect.size) * self.game.camera.zoom)
        self.game.screen.blit(renderImage, renderRect)