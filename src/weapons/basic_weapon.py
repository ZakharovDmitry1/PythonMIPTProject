# weapons/weapon.py
from abc import abstractmethod

from src.entitles.animation_sprite import AnimationSprite
from src.utils.assets_loader import GUNS_GROUP


class Weapon(AnimationSprite):
    def __init__(self, sheet: str, list_height: int, list_weight: int, x: int, y: int):
        super(Weapon, self).__init__(sheet, 1, 1, x, y, GUNS_GROUP)
        pass


    def shoot(self):
        pass

     def attack_animation(self):
         pass


