import pygame
from main import Game

class Map(object):
    def __init__(self, game:Game) -> None:
        self.game:Game = game
        self.objs:list = []
        self.entities:list = []