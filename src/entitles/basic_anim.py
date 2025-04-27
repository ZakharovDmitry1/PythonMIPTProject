import random
import threading
import time
from typing import Any

import pygame
from pygame import mixer

from src.config import TILE_SIZE, DEFAULT_DAMAGE
from src.entitles.animation_sprite import AnimationSprite
from src.entitles.enemy_dead import EnemyDead
from src.utils.assets_loader import DEAD_ENEMY_GROUP, WALLS_GROUP


class Anim(AnimationSprite):
    def __init__(self, sheet: str, list_height: int, list_weight: int, x: int,
                 y: int, speed: int = 10, hp: int = 100, resize_len: int = 75):
        '''
        Живое существо. У каждого существа может быть броня или оружие.
        Каждое может двигаться или стоять. От этого зависит анимация существа.
        Есть hp. если оно не больше нуля,то существо умирает
        :param sheet:
        :param list_for_sprites:
        :param x:
        :param y:
        :param speed:
        :param hp:
        '''
        super(Anim, self).__init__(sheet=sheet, list_weight=list_weight, list_height=list_height,
                                   x=x, y=y, resize_len=resize_len)
        self.is_moving: bool = True
        self.speed: int = speed
        self.armor = None
        self.weapon = None
        self.hp: int = hp

    def move(self, dx: float, dy: float):
        '''
        Смещает прямоугольник, rect существа в направлении движения
        :param dx: смещение по оси x
        :param dy: смещение по оси y
        :return: None
        '''
        if self.is_moving and not pygame.sprite.spritecollideany(self, WALLS_GROUP):
            self.rect = self.rect.move(dx * self.speed, dy * self.speed)
            if pygame.sprite.spritecollideany(self, WALLS_GROUP):
                self.rect = self.rect.move(-dx * self.speed, -dy * self.speed)

    def set_damage(self, hp: int):
        '''
        Это атака в героя. Если self.hp <= 0 то существо умирает
        :param hp: убирает hp дамага от героя
        :return:
        '''
        self.hp -= hp
        if self.hp <= 0:
            self.kill()

    def set_armor(self, armor):
        self.armor = armor

    def set_weapon(self, weapon=None):
        if self.weapon is not None:
            self.weapon.kill()
        self.weapon = weapon
        self.weapon.move(self.rect.x + TILE_SIZE * 4 // 6, self.rect.y + TILE_SIZE * 4 // 6)

    def kill(self) -> None:
        DEAD_ENEMY_GROUP.add(EnemyDead(self.rect.centerx, self.rect.centery))
        if random.randint(0, 100) < 10:
            k = random.randint(1, 25)
            #DropWeapon('RoguelikeWeapons/Weapons 1-Sheet.png', columns=25, rows=8, column=k,
            #           width_image=50, pos=self.rect.center, class1='Gun', gid=k)
        elif random.randint(0, 100) < 10:
            k = random.randint(1, 9)
            #DropWeapon('RoguelikeWeapons/Weapons 2-Sheet.png', columns=11, rows=8, column=random.randint(1, 9),
            #           width_image=50, pos=self.rect.center, class1='Gun', gid=(k + 25))
        if self.weapon is not None:
            self.weapon.kill()
        super(Anim, self).kill()


class EngryMob(Anim):
    def __init__(self, sheet: str, list_for_sprites: list[list[int]], x: int, y: int, speed: int, hp: int):
        super(EngryMob, self).__init__(sheet, list_for_sprites, x, y, speed, hp)
        self.way: list[tuple[int, int]] = []
        self.timer_move_way_pos: float = time.time()
        self.timer_move: float = time.time()
        self.way_pos: int = -1
        self.count_move: int = 0
        self.max_count_move: int = 15

    def set_way(self, way):
        self.way = way
        self.way_pos = 0

    def simple_move(self, dx: float, dy: float):
        self.rect = self.rect.move(dx, dy)
        # if pygame.sprite.spritecollideany(self, walls_group):
        #     self.rect.move_ip(-dx, -dy)
        #     if self.weapon is not None:
        #         self.weapon.move(-dx, -dy)

    def run(self):
        if not self.is_moving:
            return
        if self.count_move > self.max_count_move:
            self.count_move = 0
            self.way_pos += 1
        if 0 <= self.way_pos < self.way.__len__() - 2:
            dx = self.way[self.way_pos + 1][0] - self.way[self.way_pos][0]
            dy = self.way[self.way_pos + 1][1] - self.way[self.way_pos][1]
            self.simple_move(dx / self.max_count_move, dy / self.max_count_move)
        if self.way_pos == self.way.__len__() - 2:
            dx = self.way[self.way_pos + 1][0] - self.way[self.way_pos][0]
            dy = self.way[self.way_pos + 1][1] - self.way[self.way_pos][1]
            self.simple_move(dx / self.max_count_move / 2, dy / self.max_count_move / 2)
        self.count_move += 1


class AnimationMoveAnim(EngryMob):
    def __init__(self, sheet: str, list_for_sprites: list[list], x: int, y: int, speed: int = 10, hp: int = 100):
        super(AnimationMoveAnim, self).__init__(sheet, list_for_sprites, x, y, speed, hp)

    def update(self, *args: Any, **kwargs: Any) -> None:
        super().update()
        if self.cur_column == 2:
            self.cur_column = 0
        elif self.cur_column == 3:
            self.cur_column = 1

    def simple_move(self, dx: int, dy: int):
        super().simple_move(dx, dy)
        if self.weapon is not None:
            self.weapon.move(dx, dy)
        if dx > 0:
            self.cur_column = 3
        elif dx < 0:
            self.cur_column = 2
        elif dy != 0:
            if self.cur_column == 0:
                self.cur_column = 2
            if self.cur_column == 1:
                self.cur_column = 3


class FlyingCreature(EngryMob):
    def __init__(self, x: int, y: int):
        super(FlyingCreature, self).__init__(
            'v1.1 dungeon crawler 16X16 pixel pack/enemies/flying creature/fly_anim_spritesheet2.png',
            [[0] * 4 for _ in range(1)], x, y, speed=10, hp=50)
        self.song_damage = pygame.mixer.Sound('music/bat_take_damage.mp3')

    def kill(self) -> None:
        SONG_DIE_FLYING_CREATURE.play(0)
        super(FlyingCreature, self).kill()

    def set_damage(self, hp: int):
        super(FlyingCreature, self).set_damage(hp)
        self.song_damage.play(0)



class GoblinCreature(AnimationMoveAnim):
    def __init__(self, x: int, y: int):
        super(GoblinCreature, self).__init__(
            'v1.1 dungeon crawler 16X16 pixel pack/enemies/goblin/goblin.png',
            [[0] * 6 for _ in range(4)], x, y, speed=10, hp=50)

    def set_damage(self, hp: int):
        super(GoblinCreature, self).set_damage(hp)
        SONG_DAMAGE_FLYING_CREATURE.play(0)

    def kill(self) -> None:
        SONG_DIE_GOBLIN_CREATURE.play(0)
        super(GoblinCreature, self).kill()

