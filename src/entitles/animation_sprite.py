import os.path
import sys
import time
from abc import abstractmethod


import pygame.sprite
from PIL import Image

from src.config import TILE_SIZE, TIME_UPDATE_MOBS_ANIMATION
from src.utils.assets_loader import ALL_SPRITES, TILES_GROUP
from src.utils.helpers import load_image


class AnimationSprite(pygame.sprite.Sprite):
    def __init__(self, sheet: str, list_height: int, list_weight: int, x: int, y: int, resize_len=50):
        self.list_for_sprites: list[list] = [[0] * list_weight for _ in range(list_height)]

        # мы приводим картинку к нужному размеру равному resize_len
        fullname = os.getcwd() + "/../"+ sheet
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        newImage = Image.open(fullname).convert('RGBA').resize(
            (resize_len * self.list_for_sprites[0].__len__(), resize_len * self.list_for_sprites.__len__()))

        self.START_POS_X: int = x * TILE_SIZE
        self.START_POS_Y: int = y * TILE_SIZE

        newImage.save('../assets/cache/sprite.png')
        self.full_img: pygame.surface.Surface = load_image('/../assets/cache/sprite.png')
        super().__init__(ALL_SPRITES)
        self.list_for_sprites: list[list[pygame.surface.Surface]] = self.list_for_sprites
        self.cut_sheet(self.full_img, self.list_for_sprites)

        self.cur_frame: int = 0
        self.cur_column: int = 0
        self.image: pygame.Surface = self.list_for_sprites[self.cur_column][self.cur_frame]
        self.rect = self.rect.move(x * TILE_SIZE, y * TILE_SIZE)
        self.timer: float = time.perf_counter()



    @abstractmethod
    def set_row(self):
        pass

    def cut_sheet(self, sheet: pygame.Surface, list_for_sprites: list[list[pygame.surface.Surface]]):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // list_for_sprites[0].__len__(),
                                sheet.get_height() // self.list_for_sprites.__len__())
        for i in range(list_for_sprites.__len__()):
            for j in range(list_for_sprites[i].__len__()):
                frame_location = (self.rect.w * j, self.rect.h * i)
                self.list_for_sprites[i][j] = sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size))

    def update(self, *args, **kwargs) -> bool:
        if abs(self.timer - time.perf_counter()) > TIME_UPDATE_MOBS_ANIMATION:
            self.cur_frame = (self.cur_frame + 1) % len(self.list_for_sprites[self.cur_column])
            self.image = self.list_for_sprites[self.cur_column][self.cur_frame]
            self.timer: float = time.perf_counter()
            return True
        return False

