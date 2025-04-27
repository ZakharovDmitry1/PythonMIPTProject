import os
import sys
import time

import pygame
from PIL import Image

from src.config import GOLEM_WEIGHT, COEF_RESIZE_GOLEM, GOLEM_HIGHT, TILE_SIZE, TIME_UPDATE_MOBS_ANIMATION
from src.entitles.animation_sprite import AnimationSprite
from src.utils.assets_loader import SOURCE_GOLEM_STAY, ALL_SPRITES, BOSS_GROUP
from src.utils.helpers import load_image


class Boss(AnimationSprite):
    def __init__(self, x: int, y: int):
        super(Boss, self).__init__(SOURCE_GOLEM_STAY, 2, 4, x, y, 400)
        BOSS_GROUP.add(self)
        ALL_SPRITES.add(self)

    def init_sleep(self):
        pass

    def attack_arm(self):
        pass

    def run(self):
        pass

    def kill(self) -> None:
        pass

    def attack_laser(self):
        pass

    def attack_ball_lightning(self):
        pass
