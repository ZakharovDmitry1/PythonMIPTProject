import pygame

from src.world.boss_window import BossWindow
from src.world.game import Game
from src.world.start_window import StartMap

if __name__ == "__main__":
    pygame.init()
    boss_window = BossWindow()
    boss_window.load_start_window()
    boss_window.run()
    boss_window.destroy()
    pygame.quit()