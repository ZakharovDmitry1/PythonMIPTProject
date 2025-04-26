class FlyingCreature2(EngryMob):
    def __init__(self, x: int, y: int):
        super(FlyingCreature2, self).__init__(
            'v1.1 dungeon crawler 16X16 pixel pack/enemies/flying creature/bat.png',
            [[0] * 5 for _ in range(1)], x, y, speed=10, hp=50)

    def set_damage(self, hp: int):
        super(FlyingCreature2, self).set_damage(hp)
        SONG_DAMAGE_FLYING_CREATURE.play(0)

    def kill(self) -> None:
        SONG_DIE_FLYING_CREATURE.play(0)
        super(FlyingCreature2, self).kill()


class FlyingCreature3(EngryMob):
    def __init__(self, x: int, y: int):
        super(FlyingCreature3, self).__init__(
            'v1.1 dungeon crawler 16X16 pixel pack/enemies/flying creature/bat2.png',
            [[0] * 5 for _ in range(1)], x, y, speed=10, hp=50)

    def kill(self) -> None:
        SONG_DIE_FLYING_CREATURE.play(0)
        super(FlyingCreature3, self).kill()

    def set_damage(self, hp: int):
        super(FlyingCreature3, self).set_damage(hp)
        SONG_DAMAGE_FLYING_CREATURE.play(0)