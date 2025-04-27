from typing import Any

import pygame.sprite

from src.utils.helpers import load_image


class Healthbar(pygame.sprite.Sprite):
    def __init__(self, health: int):
        super(Healthbar, self).__init__(bar_group)
        self.health: int = health
        self.full_health: int = health
        self.image = load_image('Roguelike Dungeon - Asset Bundle/HUD/HP/Value/HP_Value_5.png')
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(0, 20)
        self.defence = DefenceBar(DEFENCE)

    def set_damage(self, damage: int):
        if self.defence.defence > 0:
            self.defence.set_damage(damage)
        else:
            self.health -= damage
            self.reset_bar()

    def reset_bar(self):
        if self.health / self.full_health > 4 / 5:
            self.image = load_image('Roguelike Dungeon - Asset Bundle/HUD/HP/Value/HP_Value_5.png')
        elif self.health / self.full_health > 3 / 5:
            self.image = load_image('Roguelike Dungeon - Asset Bundle/HUD/HP/Value/HP_Value_4.png')
        elif self.health / self.full_health > 2 / 5:
            self.image = load_image('Roguelike Dungeon - Asset Bundle/HUD/HP/Value/HP_Value_3.png')
        elif self.health / self.full_health > 1 / 5:
            self.image = load_image('Roguelike Dungeon - Asset Bundle/HUD/HP/Value/HP_Value_2.png')
        elif self.health / self.full_health > 0 / 5:
            self.image = load_image('Roguelike Dungeon - Asset Bundle/HUD/HP/Value/HP_Value_1.png')
        else:
            self.image = load_image('Roguelike Dungeon - Asset Bundle/HUD/HP/Value/HP_Value_0.png')

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.reset_bar()


class DefenceBar(pygame.sprite.Sprite):
    def __init__(self, defence: int):
        super(DefenceBar, self).__init__(bar_group)
        self.defence: int = defence
        self.full_defence: int = defence
        self.image = load_image('Roguelike Dungeon - Asset Bundle/HUD/Defence/Value/Defence_Value_5.png')
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(0, 0)

    def set_damage(self, damage: int):
        self.defence -= damage
        if self.defence < 0:
            self.defence = 0
        self.reset_bar()

    def reset_bar(self):
        if self.defence / self.full_defence > 4 / 5:
            self.image = load_image('Roguelike Dungeon - Asset Bundle/HUD/Defence/Value/Defence_Value_5.png')
        elif self.defence / self.full_defence > 3 / 5:
            self.image = load_image('Roguelike Dungeon - Asset Bundle/HUD/Defence/Value/Defence_Value_4.png')
        elif self.defence / self.full_defence > 2 / 5:
            self.image = load_image('Roguelike Dungeon - Asset Bundle/HUD/Defence/Value/Defence_Value_3.png')
        elif self.defence / self.full_defence > 1 / 5:
            self.image = load_image('Roguelike Dungeon - Asset Bundle/HUD/Defence/Value/Defence_Value_2.png')
        elif self.defence / self.full_defence > 0 / 5:
            self.image = load_image('Roguelike Dungeon - Asset Bundle/HUD/Defence/Value/Defence_Value_1.png')
        else:
            self.image = load_image('Roguelike Dungeon - Asset Bundle/HUD/Defence/Value/Defence_Value_0.png')
