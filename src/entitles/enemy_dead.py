from typing import Any

from src.entitles.animation_sprite import AnimationSprite


class EnemyDead(AnimationSprite):
    def __init__(self, x: int, y: int):
        '''
        :param x: координата x эффекта смерти
        :param y: координата y эффекта смерти
        '''
        super().__init__(r"assets\affects\enemy_afterdead_explosion_anim_spritesheet.png", 1, 5, x=x, y=y, resize_len=75)
        self.rect.centerx = x
        self.rect.centery = y
        self.count: int = 0

    def update(self, *args: Any, **kwargs: Any) -> None:
        f: bool = super(EnemyDead, self).update()
        if f:
            self.count += 1
        if self.count == self.list_for_sprites[0].__len__():
            self.kill()