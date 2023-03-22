from pygame import Vector2, key
from pygame.locals import *
from math import sqrt

class Camera(object):
    def __init__(self, game, pos:Vector2=Vector2(0, 0), zoom:float=1.0, movementSpeed:float=2.5, movementBrake:float=0.05, zoomSpeed:float=0.025) -> None:
        self.game = game
        self.zoom:float = zoom
        self.zoomSpeed = zoomSpeed
        self.speed:float = movementSpeed
        self.brake:float = 1 - movementBrake
        self.pos:Vector2 = pos
        self.vel:Vector2 = Vector2(0, 0)
        self.acc:Vector2 = Vector2(0, 0)
        
    def getOnScreenPos(self, vector:Vector2) -> Vector2:
        screenPos = vector * self.zoom - self.pos
        # if screenPos.x < -self.game.res.x * outsideBouds or screenPos.x > self.game.res.x * (outsideBouds + 1) or \
        #     screenPos.y < -self.game.res.y * outsideBouds or screenPos.y > self.game.res.y * (outsideBouds + 1):
        return screenPos
        
    def getRealWorldPos(self, vector:Vector2) -> Vector2:
        return (vector + self.pos) / self.zoom
    
    def update(self) -> None:
        keys = key.get_pressed()
        self.acc *= 0
        if keys[K_w]:
            self.acc += Vector2(0, -self.speed * sqrt(self.zoom))
        if keys[K_s]:
            self.acc += Vector2(0, self.speed * sqrt(self.zoom))
        if keys[K_a]:
            self.acc += Vector2(-self.speed * sqrt(self.zoom), 0)
        if keys[K_d]:
            self.acc += Vector2(self.speed * sqrt(self.zoom), 0)
        if keys[K_q]:
            self.zoom *= 1 + self.zoomSpeed
        if keys[K_e]:
            self.zoom *= 1 - self.zoomSpeed
            
        self.vel += self.acc
        self.pos += self.vel
        
        self.vel *= self.brake
            