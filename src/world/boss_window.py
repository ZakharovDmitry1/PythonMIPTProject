import csv
import json
import os
import time

import pygame

from src.config import TILE_SIZE, TIME_UPDATE_MOBS_ANIMATION
from src.entitles.boss import Boss
from src.entitles.player import Player
from src.entitles.title import Tile2
from src.utils.assets_loader import WALLS_GROUP, TILES_GROUP, LAVA_GROUP
from src.utils.helpers import processor_buttons
from src.world.basic_window import BasicWindow

class BossWindow(BasicWindow):
    def __init__(self):
        super(BossWindow, self).__init__()
        self.player = Player(10, 10)
        self.boss = Boss(20, 20)

    def load_start_window(self):
        '''
        Загрузка стартовой локации из файла boss.csv
        В файле tiles_for_start_map.json находятся ссылки на все картинки
        '''
        self.map: list[list[int]] = []
        # Получаем абсолютный путь к директории, где находится текущий скрипт
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Строим абсолютный путь к файлу
        file_path = os.path.join(script_dir, '../../levels/boss_window/boss_map.csv')
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for index, row in enumerate(reader):
                self.map.append(list(map(int, row)))
        # Строим абсолютный путь к файлу
        file_path = os.path.join(script_dir, '../../levels/boss_window/tiles_for_start_map.json')
        with open(file_path, 'r') as readfile:
            self.tiles_for_start_map: dict = json.load(readfile)
        for i in range(self.map.__len__()):
            for j in range(self.map[0].__len__()):
                tile = Tile2(self.tiles_for_start_map[str(self.map[i][j])], j, i, resize=TILE_SIZE)
                if 5 <= self.map[i][j] <= 19:
                    WALLS_GROUP.add(tile)
                elif 20 <= self.map[i][j] <= 48:
                    TILES_GROUP.add(tile)
                elif self.map[i][j] == 49:
                    LAVA_GROUP.add(tile)
