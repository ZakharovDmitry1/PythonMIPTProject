# game.py
import time

import pygame

from src.config import FPS, WIDTH, HEIGHT, TIME_UPDATE_MOBS_ANIMATION
from src.entitles.player import Player
from src.entitles.title import Tile
from src.utils.assets_loader import ALL_SPRITES, TILES_GROUP, PLAYER_GROUP, DEAD_ENEMY_GROUP, GUNS_GROUP
from src.utils.helpers import load_level, processor_buttons
from src.world.basic_window import BasicWindow
from src.world.camera import Camera


class Game(BasicWindow):
    def __init__(self):
        super(Game, self).__init__()

    def load_assets(self):
        pass
        # Используйте utils/assets_loader.py для централизованной загрузки


    def generate_level(self):
        '''
        Генерация уровня
        '''
        level = load_level('levels/level.txt')
        for y in range(len(level)):
            for x in range(len(level[y])):
                if level[y][x] == '.':
                    Tile('empty', x, y)
                elif level[y][x] == '#':
                    Tile('wall', x, y)
                elif level[y][x] == '@':
                    Tile('empty', x, y)
                    self.player = Player(x, y)


    def handle_events(self):
        pass