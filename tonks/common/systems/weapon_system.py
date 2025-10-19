
import esper
import pygame

from tonks.common.components import  Position,  Turret, Weapon
from tonks.common.entities import spawn_bullet

class WeaponSystem(esper.Processor):
    def process(self, dt):
        mouse_pressed = pygame.mouse.get_pressed()[0]  # 0 = left button
        for _ent, (pos, turret, weapon) in esper.get_components(Position, Turret, Weapon):
            weapon.timer -= dt
            if mouse_pressed and weapon.timer <= 0:
                weapon.timer = weapon.cooldown
                spawn_bullet(pos, turret, weapon)
