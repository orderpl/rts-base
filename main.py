import pygame
from pygame import Vector2, Surface, time, font
from hut import Hut
from map import Map
from camera import Camera
from building import Building
from resourcesController import ResourceController as RC

pygame.init()
font.init()

class Game(object):
    def __init__(self, screenSize:Vector2 | tuple[int, int]=Vector2(0, 0)) -> None:
        self.screen:Surface = pygame.display.set_mode(screenSize)
        self.res:Vector2 = Vector2(pygame.display.get_window_size())
        self.running:bool = True
        self.deltaTime:float = 0.0
        self.clock:time.Clock = time.Clock()
        self.camera:Camera = Camera(self, movementSpeed=1.2, movementBrake=0.1)
        self.tps:int = 60
        
        self.fontNormal = font.SysFont("Arial", 20)
        self.rc = RC(self)
        self.map:Map = Map(self)
    
    def writeText(self, text:str, pos:Vector2, customFont:font.SysFont, out=False):
        r = customFont.render(text, True, (255, 255, 255))
        if out:
            return r
        else:
            self.screen.blit(r, pos)

    def run(self) -> None:
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

            self.deltaTime += self.clock.tick() / 1000.0
            while self.deltaTime > 1 / self.tps:
                self.camera.update()
                
                if pygame.mouse.get_pressed()[0]:
                    newB = Hut(self, self.camera.getRealWorldPos(Vector2(pygame.mouse.get_pos())))
                    self.tryPlaceBuilding(newB)
                    
                self.rc.update()
                
                    
                self.deltaTime -= 1 / self.tps
    
            self.render()
            
            pygame.display.set_caption(f"{int(self.clock.get_fps())}")
        pygame.quit()
    
    def render(self):
        self.map.render()
        self.rc.renderUI()

        pygame.display.update()
        self.screen.fill((0, 0, 0))

    def tryPlaceBuilding(self, building: Building) -> None:        
        for obj in self.map.objs:
            if obj.rect.colliderect(building.rect):
                return
        if isinstance(building, Hut):
            self.rc.maxHousing += 2
        self.map.objs.append(building)
        
if __name__ == "__main__":
    game = Game(Vector2(1600, 900))
    game.run()