WIDTH, HEIGHT = 1280, 720
MONITOR_WIDTH, MONITOR_HEIGHT = 1280, 720
FPS: int = 60
TILE_SIZE: int = 64
PLAYER_SPEED: int = 400
GOLEM_HIGHT: int = 50
GOLEM_WEIGHT: int = 54
COEF_RESIZE_GOLEM: float = 1
COLORS = {
    'background': (30, 30, 46),
    'ui': (137, 180, 250)
}
BLOCKS = {
    'wall' : "assets/blocks/wall.png",
    'empty' : 'assets/blocks/wall.png',
    'grass' : 'assets/blocks/wall.png'
}
TIME_UPDATE_MOBS_ANIMATION: float = 0.1
TIME_UPDATE_WEAPON_ANIMATION: float = 0.05
DEFAULT_DAMAGE: int = 10
TIME_MOVE_MOBS = 0.1