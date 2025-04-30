import math
import time

import pygame

from src.config import TILE_SIZE
from src.entitles.animation_sprite import AnimationSprite
from src.utils.assets_loader import WALLS_GROUP, MOBS_GROUP, BULLET_GROUP, ALL_SPRITES


class Bullet(AnimationSprite):
    def __init__(self, sheet, x, y, target_x, target_y, speed, time_die, damage, size):
        '''
        пуля, всегда летит по прямой. Если ударяется об стену, умирает
        :param sheet:
        :param x: начало вылета x
        :param y: начало вылета y
        :param target_x: направление вылета x
        :param target_y: направление вылета y
        :param speed: скорость пули
        :param time_die: время жизни пули
        :param damage: урон
        :param size: размер спрайта
        '''
        super(Bullet, self).__init__(sheet, 1, 1, x // TILE_SIZE, y // TILE_SIZE, size)
        BULLET_GROUP.add(self)
        ALL_SPRITES.add(self)
        self.TARGET_POS_X = target_x
        self.TARGET_POS_Y = target_y
        self.speed = speed
        self.time_start = time.time()
        self.time_die = time_die
        self.damage = damage

        # высчитываем вектор единичной длинны в направлении пули
        delta_x = target_x - x
        delta_y = target_y - y
        len_vector = math.sqrt(delta_x * delta_x + delta_y * delta_y)
        self.dx = delta_x / len_vector
        self.dy = delta_y / len_vector
        self.rect = pygame.Rect(x, y, size, size)

    def move(self):
        self.rect = self.rect.move(self.dx * self.speed, self.dy * self.speed)
        if pygame.sprite.spritecollideany(self, WALLS_GROUP) or time.time() - self.time_start >= self.time_die:
            self.kill()
        for i in MOBS_GROUP:
            if pygame.sprite.collide_rect(i, self):
                i.set_damage(self.damage)
                self.kill()

    def update(self, *args, **kwargs):
        self.move()


class Bullet1(Bullet):
    def __init__(self, x, y, target_x, target_y):
        super(Bullet1, self).__init__('assets/sprites/bullets/Bullets 1-Sheet (0_0).png', x, y, target_x, target_y, 10,
                                      10, 10, 40)
