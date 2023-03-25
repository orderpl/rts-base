from building import Building

class Map(object):
    def __init__(self, game) -> None:
        self.game = game
        self.objs:list[Building, ] = []
        self.entities:list = []
        
    def render(self) -> None:
        for obj in self.objs:
            obj.render()