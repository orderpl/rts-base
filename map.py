from building import Building
from pygame import Vector2

class Map(object):
    def __init__(self, game) -> None:
        self.game = game
        self.objs:list[Building, ] = []
        self.entities:list = []
        
    def render(self) -> None:
        objsToRender = []
        for obj in self.objs:
            topleft = self.game.camera.getOnScreenPos(Vector2(obj.rect.topleft))
            bottomright = self.game.camera.getOnScreenPos(Vector2(obj.rect.bottomright))
            if not ((topleft.x < 0 and bottomright.x < 0) or (topleft.x > self.game.res.x and bottomright.x > self.game.res.x) or \
                    (topleft.y < 0 and bottomright.y < 0) or (topleft.y > self.game.res.y and bottomright.y > self.game.res.y)):
                objsToRender.append(obj)
        objsToRender.sort(key=lambda x: x.rect.bottom)
            
        for obj in objsToRender:
            obj.render()