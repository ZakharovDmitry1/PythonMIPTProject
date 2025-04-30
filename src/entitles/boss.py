import os
import sys
import time

import pygame
from PIL import Image

from src.config import GOLEM_WEIGHT, COEF_RESIZE_GOLEM, GOLEM_HIGHT, TILE_SIZE, TIME_UPDATE_MOBS_ANIMATION
from src.entitles.animation_sprite import AnimationSprite
from src.entitles.player import Player
from src.utils.assets_loader import SOURCE_GOLEM_STAY, ALL_SPRITES, BOSS_GROUP, MOBS_GROUP, SOURCE_GOLEM_DIE, \
    PLAYER_GROUP
from src.utils.helpers import load_image

BOSS_KILL_TIME_SPRITE_FLIP = 0.2


class Boss(AnimationSprite):
    def __init__(self, x: int, y: int):
        super(Boss, self).__init__(SOURCE_GOLEM_STAY, 2, 4, x, y, 300)
        BOSS_GROUP.add(self)
        MOBS_GROUP.add(self)
        ALL_SPRITES.add(self)
        self.hp = 10
        self.speed = 7  # Скорость движения
        self.target = None  # Цель (игрок)

    def _find_player(self):
        """Поиск игрока в группе спрайтов."""
        for sprite in PLAYER_GROUP:
            if isinstance(sprite, Player):
                self.target = sprite
                return
        self.target = None  # Игрок не найден

    def run(self):
        """Движение к игроку."""
        if not self.target:
            self._find_player()
            if not self.target:
                return  # Игрок всё ещё не найден

        # Рассчитать направление
        dx = self.target.rect.centerx - self.rect.centerx
        dy = self.target.rect.centery - self.rect.centery
        distance = (dx ** 2 + dy ** 2) ** 0.5

        # Нормализация вектора
        if distance > 0:
            move_x = (dx / distance) * self.speed
            move_y = (dy / distance) * self.speed
            self.rect.x += move_x
            self.rect.y += move_y

        # Обработка направления спрайта (влево/вправо)
        if dx < 0:
            self.image = pygame.transform.flip(self.image, True, False)
        elif dx > 0:
            self.image = pygame.transform.flip(self.image, False, False)

    def update(self, *args, **kwargs) -> bool:
        if super().update():
            self.run()
            return True
        return False


    def init_sleep(self):
        pass

    def attack_arm(self):
        pass

    def kill(self) -> None:
        super(Boss, self).kill()

    def attack_laser(self):
        pass

    def attack_ball_lightning(self):
        pass

    def set_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.kill()

class BossDie(AnimationSprite):
    def __init__(self, x, y):
        super(BossDie, self).__init__(SOURCE_GOLEM_STAY, 1, 8, x, y, 300)
        #ALL_SPRITES.add(self)
        BOSS_GROUP.add(self)

    def update(self, *args, **kwargs) -> bool:
        if super(BossDie, self).update():
            print("AAAAAAAAAAAAAAA")
            if self.cur_frame == len(self.list_for_sprites[self.cur_column]) - 1:
                self.kill()
            return True
        return False