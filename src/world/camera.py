import pygame
from src.config import MONITOR_WIDTH, MONITOR_HEIGHT


class Camera:
    def __init__(self):
        self.dx: int = 0
        self.dy: int = 0

    def apply(self, obj: pygame.sprite.Sprite):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target: pygame.sprite.Sprite):
        self.dx = - (target.rect.x + target.rect.w // 2 - MONITOR_WIDTH // 2 - 20)
        self.dy = - (target.rect.y + target.rect.h // 2 - MONITOR_HEIGHT // 2 - 20)
