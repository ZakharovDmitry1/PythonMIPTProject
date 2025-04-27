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
    start_window = StartMap()
    start_window.load_start_window()
    start_window.run()
    start_window.destroy()
    game = Game()
    game.generate_level()
    game.run()
    pygame.quit()