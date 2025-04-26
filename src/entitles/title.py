import os

import pygame
from PIL import Image

from src.config import TILE_SIZE, BLOCKS
from src.utils.assets_loader import TILES_GROUP, ALL_SPRITES
from src.utils.helpers import load_image


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type: str, pos_x: int, pos_y: int, colorkey: tuple = (0, 0, 0), resize: int = TILE_SIZE,
                 set_tile_size: bool = False):
        super().__init__(TILES_GROUP, ALL_SPRITES)
        source = '/../' + BLOCKS[tile_type]
        self.image = load_image(source)
        self.image.set_colorkey(colorkey)
        if resize != -1:
            newImage = Image.open(source).convert('RGBA').resize((resize, resize))
            newImage.save('../../assets/cache/wall.png')
            self.image = load_image('/../assets/cache/wall.png')
            self.image.set_colorkey(colorkey)
        if set_tile_size:
            self.rect = pygame.rect.Rect(TILE_SIZE * pos_x, TILE_SIZE * pos_y, TILE_SIZE, TILE_SIZE)
        else:
            self.rect = self.image.get_rect().move(
                TILE_SIZE * pos_x, TILE_SIZE * pos_y)


class Tile2(pygame.sprite.Sprite):
    def __init__(self, source: str, pos_x: int, pos_y: int, colorkey: tuple = (0, 0, 0), resize: int = -1,
                 set_tile_size: bool = False):
        super().__init__(TILES_GROUP, ALL_SPRITES)
        source = '/../' + source
        self.image = load_image(source)
        self.image.set_colorkey(colorkey)
        if resize != -1:
            newImage = Image.open(os.getcwd() + source).convert('RGBA').resize((resize, resize))
            newImage.save(os.getcwd() + '/../assets/cache/wall.png')
            self.image = load_image('/../assets/cache/wall.png')
            self.image.set_colorkey(colorkey)
        if set_tile_size:
            self.rect = pygame.rect.Rect(TILE_SIZE * pos_x, TILE_SIZE * pos_y, TILE_SIZE, TILE_SIZE)
        else:
            self.rect = self.image.get_rect().move(
                TILE_SIZE * pos_x, TILE_SIZE * pos_y)
