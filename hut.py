from building import Building
from pygame import Vector2
from images import IMAGES

class Hut(Building):
    def __init__(self, game, center:Vector2) -> None:
        image = IMAGES["hut"]
        rect = image.get_rect(center=center)
        super().__init__(game, image, rect, Vector2(0, 0))
        