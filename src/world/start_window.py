import csv
import json
import os
import time

import pygame
from _distutils_hack import override

from src.config import TILE_SIZE, TIME_UPDATE_MOBS_ANIMATION
from src.entitles.player import Player
from src.entitles.title import Tile, Tile2
from src.utils.assets_loader import WALLS_GROUP, TILES_GROUP, LAVA_GROUP
from src.utils.helpers import processor_buttons
from src.world.basic_window import BasicWindow


class StartMap(BasicWindow):
    def __init__(self):
        super(StartMap, self).__init__()
        self.player = Player(10, 10)

    def load_start_window(self):
        '''
        Загрузка стартовой локации из файла boss.csv
        В файле tiles_for_start_map.json находятся ссылки на все картинки
        '''
        self.map: list[list[int]] = []
        # Получаем абсолютный путь к директории, где находится текущий скрипт
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Строим абсолютный путь к файлу
        file_path = os.path.join(script_dir, '../../levels/start_window/boss.csv')
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for index, row in enumerate(reader):
                self.map.append(list(map(int, row)))
        # Строим абсолютный путь к файлу
        file_path = os.path.join(script_dir, '../../levels/start_window/tiles_for_start_map.json')
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

    def run(self):
        '''
        главное окно экрана
        Здесь отририсовывается все
        :return:
        '''
        time_move_mobs: float = time.time()
        running: bool = True
        if not hasattr(self, 'player'):
            print("player is not defined")
            pygame.quit()
            exit()
            return
        while running:
            if time.time() - time_move_mobs >= TIME_UPDATE_MOBS_ANIMATION:
                time_move_mobs = time.time()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            processor_buttons(self.player)
            self.screen.fill((255, 255, 255))
            self.update()
            self.draw()
            for i in LAVA_GROUP:
                if i.rect.collidepoint(self.player.rect.center):
                    running = False
