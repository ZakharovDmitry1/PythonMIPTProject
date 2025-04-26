from __future__ import annotations

import math
import os
import sys

import pygame
from pygame import SurfaceType, Surface


def load_image(filename: str, colorkey=None) -> Surface | SurfaceType:
    fullname = os.getcwd() + filename
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def len_to_points(a: tuple[float, float], b: tuple[float, float]) -> float:
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def load_level(filename):
    fullname = os.getcwd() + "/../" + filename
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    with open(fullname, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def processor_buttons(player):
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_RIGHT] and keys[pygame.K_UP]) or (keys[pygame.K_w] and keys[pygame.K_d]):
        player.move(0.35, -0.35)
    elif (keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]) or (keys[pygame.K_d] and keys[pygame.K_s]):
        player.move(0.35, 0.35)
    elif (keys[pygame.K_DOWN] and keys[pygame.K_LEFT]) or (keys[pygame.K_s] and keys[pygame.K_a]):
        player.move(-0.35, 0.35)
    elif (keys[pygame.K_LEFT] and keys[pygame.K_UP]) or (keys[pygame.K_a] and keys[pygame.K_w]):
        player.move(-0.35, -0.35)
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.move(-0.5, 0)
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.move(0.5, 0)
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.move(0, 0.5)
    elif keys[pygame.K_UP] or keys[pygame.K_w]:
        player.move(0, -0.5)
