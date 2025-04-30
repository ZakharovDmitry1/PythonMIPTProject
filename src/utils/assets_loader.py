import pygame

SOURCE_KNIGHT = 'assets/sprites/characters/knight/knight_sprite.png'
SOURCE_MAG = 'assets/sprites/characters/mag/mag.png'
SOURCE_GOLEM_STAY = 'assets/boss/GolemStay.png'
SOURCE_GOLEM_DIE = 'assets/boss/Golem2.png'

ALL_SPRITES = pygame.sprite.Group()
TILES_GROUP = pygame.sprite.Group()
WALLS_GROUP = pygame.sprite.Group()
MOBS_GROUP = pygame.sprite.Group()
PLAYER_GROUP = pygame.sprite.Group()
DEAD_ENEMY_GROUP = pygame.sprite.Group()
GUNS_GROUP = pygame.sprite.Group()
LAVA_GROUP = pygame.sprite.Group()
BOSS_GROUP = pygame.sprite.Group()
BULLET_GROUP = pygame.sprite.Group()