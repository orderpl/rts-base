import pygame
from pygame import Vector2, Surface, time, font
from map import Map
from camera import Camera
from building import Building

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
        
        self.map:Map = Map(self)
        # self.map.objs.append(Building(self, Surface(Vector2(1, 1)), pygame.Rect(0, 0, 100, 100)))
    
    def writeText(self, text:str, pos:Vector2, usedFont:font.SysFont=font.SysFont("Arial", 20), out=False):
        r = usedFont.render(text, 1, (255, 255, 255))
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
                    newRect = pygame.Rect(Vector2(0, 0), Vector2(100, 100))
                    newRect.center = self.camera.getRealWorldPos(pygame.mouse.get_pos())
                    canPlace = True
                    for obj in self.map.objs:
                        if obj.rect.colliderect(newRect):
                            canPlace = False
                            break
                    if canPlace:
                        self.map.objs.append(Building(self, Surface(Vector2(1, 1)), newRect))
                    
                self.deltaTime -= 1 / self.tps
                    
            ########################################################################################################################################################
    
            self.map.render()

            pygame.display.set_caption(f"{int(self.clock.get_fps())}")
            pygame.display.update()
            self.screen.fill((0, 0, 0))
        pygame.quit()
        
if __name__ == "__main__":
    game = Game(Vector2(800, 450))
    game.run()