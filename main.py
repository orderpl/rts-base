import pygame
from pygame import Vector2, Surface, time

class Game(object):
    def __init__(self, screen_size:Vector2 | tuple[int, int]=Vector2(0, 0)) -> None:
        self.screen:Surface = pygame.display.set_mode(screen_size)
        self.res:Vector2 = Vector2(pygame.display.get_window_size())
        self.running:bool = True
        self.deltaTime:float = 0.0
        self.clock:time.Clock = time.Clock()
    
    def run(self) -> None:
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False                

            pygame.display.update()
            self.screen.fill((0, 0, 0))
            self.deltaTime += self.clock.tick()
        pygame.quit()
        
if __name__ == "__main__":
    game = Game(Vector2(800, 450))
    game.run()