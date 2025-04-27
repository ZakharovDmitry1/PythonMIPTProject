# weapons/weapon.py
import os
import time
from abc import abstractmethod

import pygame
from PIL import Image

from src.config import TIME_UPDATE_MOBS_ANIMATION, TILE_SIZE
from src.entitles.animation_sprite import AnimationSprite
from src.utils.assets_loader import GUNS_GROUP, ALL_SPRITES
from src.utils.helpers import load_image
from src.weapons.bullets.bullet import Bullet, Bullet1


class Weapon(AnimationSprite):
    def __init__(self, sheet: str, max_row, x: int, y: int, size_weapon, cooldown):
        super(Weapon, self).__init__(sheet, 1, 8, x // TILE_SIZE, y // TILE_SIZE, size_weapon)
        self.rect = pygame.Rect(x, y, size_weapon, size_weapon)
        GUNS_GROUP.add(self)
        self.max_row = max_row
        self.time_last_attack = time.time()
        self.cooldown = cooldown

    def attack(self, target_x, target_y):
        if time.time() - self.time_last_attack < self.cooldown:
            return
        self.time_last_attack = time.time()
        Bullet1(self.rect.centerx, self.rect.centery, target_x, target_y)

    def update(self, *args, **kwargs):
        if abs(self.timer - time.perf_counter()) > TIME_UPDATE_MOBS_ANIMATION:
            self.cur_frame = 0 #(self.cur_frame + 1) % self.max_row
            self.image = self.list_for_sprites[0][self.cur_frame]

    def move(self, pos_x, pos_y):
        self.rect = self.rect.move(pos_x, pos_y)



class Gun(Weapon):
    def __init__(self, x, y):
        super(Gun, self).__init__('assets/sprites/weapons/weapons1/25.png', 3, x, y, 64, 1)
