import pygame
from pygame import Surface, Vector2

class Camera(object):
    def __init__(self, pos:Vector2=Vector2(0, 0), zoom:float=1.0) -> None:
        self.pos:Vector2 = pos
        self.zoom:float = zoom