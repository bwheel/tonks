import sys
from typing import Tuple
from contextlib import contextmanager

import esper
import pygame

from tonks.common import constants
from tonks.common import entities
from tonks.common.systems.bullet_system import BulletSystem
from tonks.common.systems.movement_system import MovementSystem
from tonks.common.systems.render_bullet_system import RenderBulletSystem
from tonks.common.systems.render_tank_system import RenderTankSystem
from tonks.common.systems.turret_system import TurretSystem
from tonks.common.systems.weapon_system import WeaponSystem

@contextmanager
def open_window(window_size: Tuple[int, int]):
    try:
        pygame.init()
        screen = pygame.display.set_mode(window_size)
        yield screen
    finally:
        if pygame.get_init():
            pygame.quit()

def main():
    with open_window((1920, 1080)) as screen:
        
        entities.spawn_player(500, 500, constants.PLAYER_COLOR)

        esper.add_processor(RenderTankSystem(screen))
        esper.add_processor(RenderBulletSystem(screen))
        esper.add_processor(MovementSystem())
        esper.add_processor(TurretSystem())
        esper.add_processor(WeaponSystem())
        esper.add_processor(BulletSystem())

        running = True
        clock = pygame.time.Clock()
        dt = 0
        while running:
            dt = clock.tick(60) / 1000.0 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill(constants.BACKGROUND_COLOR)
            esper.process(dt)
            pygame.display.flip()



if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print(str(ex))
        sys.exit(1)

