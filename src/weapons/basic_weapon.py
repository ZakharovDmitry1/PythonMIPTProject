# weapons/weapon.py
import math
import os
import time
from abc import abstractmethod

import pygame
from PIL import Image
from pygame.surface import Surface

from src.config import TIME_UPDATE_MOBS_ANIMATION, TILE_SIZE, TIME_UPDATE_WEAPON_ANIMATION
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
        self.is_attack = False
        self.angle = 0

    def attack(self, target_x, target_y):
        if time.time() - self.time_last_attack < self.cooldown:
            return
        self.is_attack = True
        self.time_last_attack = time.time()
        Bullet1(self.rect.centerx, self.rect.centery, target_x, target_y)

    def set_angle(self):
        target_x, target_y = pygame.mouse.get_pos()
        # высчитываем угол поворота оружия
        vector = (target_x - self.rect.centerx, target_y - self.rect.centery)
        # косинус между vector и (1, 0)
        cos_a = vector[0] / math.sqrt(vector[1] * vector[1] + vector[0] * vector[0])

        self.angle = math.acos(cos_a)
        self.vector = vector

    def rotate_image(self):
        self.image = pygame.transform.rotate(self.list_for_sprites[0][self.cur_frame], math.degrees(self.angle))
        if self.vector[1] > 0:
            self.image = pygame.transform.flip(self.image, False, True)


    def update(self, *args, **kwargs):
        self.set_angle()
        if abs(self.timer - time.perf_counter()) > TIME_UPDATE_WEAPON_ANIMATION:
            if self.is_attack:
                print(self.angle)
                self.cur_frame = (self.cur_frame + 1) % self.max_row
                if self.cur_frame == 0:
                    self.is_attack = False
            self.rotate_image()
            self.timer = time.perf_counter()

    def move(self, pos_x, pos_y):
        self.rect = self.rect.move(pos_x, pos_y)



class Gun(Weapon):
    def __init__(self, x, y):
        super(Gun, self).__init__('assets/sprites/weapons/weapons1/25.png', 3, x, y, 64, 1)
