import pygame
from pygame import Surface, Vector2, Rect

debug = False

class Building(object):
    def __init__(self, game, image:Surface, rect:Rect, imageOffset:Vector2, imageSize:Vector2) -> None:
        """Image offset is offset from center"""
        self.game = game
        self.imageOffset = imageOffset
        self.image:Surface = pygame.transform.scale(image, imageSize)
        self.imageRect:Rect = self.image.get_rect()
        self.rect:Rect = rect # position on the map
        
    def render(self) -> None:
        renderImage = pygame.transform.scale(self.image, Vector2(self.imageRect.size) * self.game.camera.zoom)
        renderRect = renderImage.get_rect(center=self.game.camera.getOnScreenPos(Vector2(self.rect.center)) + self.imageOffset)
        if debug:
            pygame.draw.rect(self.game.screen, (159, 255, 159), renderRect)
        self.game.screen.blit(renderImage, renderRect)