import pygame
from pygame import mixer

mixer.init()

SONG_MAIN_PLAY: pygame.mixer.Sound = pygame.mixer.Sound('music/stranger-things-124008.mp3')
SONG_START_PLAY: pygame.mixer.Sound = pygame.mixer.Sound('music/song18.mp3')
SONG_DIE_FLYING_CREATURE: pygame.mixer.Sound = pygame.mixer.Sound('music/bat_die.mp3')
SONG_DAMAGE_FLYING_CREATURE: pygame.mixer.Sound = pygame.mixer.Sound('music/bat_take_damage.mp3')
SONG_DIE_GOBLIN_CREATURE: pygame.mixer.Sound = pygame.mixer.Sound('music/gladiator_die.mp3')
GUN_ATTACK: pygame.mixer.Sound = pygame.mixer.Sound('music/vystrel-s-pistoleta.mp3')