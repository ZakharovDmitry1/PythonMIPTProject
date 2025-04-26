import sys
import time
from typing import Any

import pygame

from src.config import TILE_SIZE, TIME_MOVE_MOBS
from src.entitles.animation_sprite import AnimationSprite
from src.entitles.basic_anim import Anim
from src.utils.assets_loader import PLAYER_GROUP, SOURCE_KNIGHT, SOURCE_MAG
from src.utils.helpers import load_image


class Player(Anim):
    def __init__(self, pos_x, pos_y, type='knight'):
        source = ''
        list_height = -1
        list_weight = -1
        if type == 'mag':
            source = SOURCE_MAG
            list_height = 4
            list_weight = 4
        elif type == 'knight':
            source = SOURCE_KNIGHT
            list_height = 4
            list_weight = 6
        else:
            print("Такого персонажа не бывает")
            pygame.quit()
            sys.exit()
        super().__init__(sheet=source, list_height=list_height, list_weight=list_weight,
                         x=pos_x, y=pos_y, speed=10, hp=100, resize_len=75)
        PLAYER_GROUP.add(self)

    def update(self, *args: Any, **kwargs: Any) -> None:
        super().update()

    def move(self, dx: float, dy: float):
        if time.time() - self.timer < TIME_MOVE_MOBS:
            return
        super(Player, self).move(dx, dy)
        if self.weapon is not None:
            self.weapon.move(dx * self.speed, dy * self.speed)
        elif dx > 0:
            self.cur_column = 3
        elif dx < 0:
            self.cur_column = 2
        elif dy != 0:
            if self.cur_column == 0:
                self.cur_column = 2
            if self.cur_column == 1:
                self.cur_column = 3