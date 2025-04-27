# game.py
import csv
import os
import time

import pygame

from src.config import FPS, WIDTH, HEIGHT, TIME_UPDATE_MOBS_ANIMATION
from src.entitles.player import Player
from src.entitles.title import Tile
from src.utils.assets_loader import ALL_SPRITES, TILES_GROUP, PLAYER_GROUP, DEAD_ENEMY_GROUP, GUNS_GROUP, BOSS_GROUP, \
    BULLET_GROUP, LAVA_GROUP
from src.utils.helpers import load_level, processor_buttons
from src.world.camera import Camera


class BasicWindow:
    def __init__(self):
        pygame.display.set_caption("Soul_Knight")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.states = {}  # Стек состояний (меню, игра и т.д.)
        self.load_assets()
        self.camera = Camera()

    def load_assets(self):
        pass
        # Используйте utils/assets_loader.py для централизованной загрузки

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
            processor_buttons(self.player)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.player.attack(event.pos)
            self.screen.fill((255, 255, 255))
            self.update()
            self.draw()
            for i in LAVA_GROUP:
                if i.rect.collidepoint(self.player.rect.center):
                    running = False

    def update(self):
        '''
        делаем сдвиг всех спрайтов относительно экрана
        :return:
        '''
        self.camera.update(self.player)  # Обновляем позицию камеры
        for sprite in ALL_SPRITES:
            sprite.update()
            self.camera.apply(sprite)  # Сдвигаем все спрайты

    def draw(self):
        '''
        Отрисовываем все title в кадре
        :return:
        '''
        TILES_GROUP.draw(self.screen)
        DEAD_ENEMY_GROUP.draw(self.screen)
        PLAYER_GROUP.draw(self.screen)
        GUNS_GROUP.draw(self.screen)
        BULLET_GROUP.draw(self.screen)
        BOSS_GROUP.draw(self.screen)
        GUNS_GROUP.draw(self.screen)
        pygame.display.flip()

    def destroy(self):
        '''
        удаляем всех спрайтов
        :return:
        '''
        for i in ALL_SPRITES:
            i.kill()