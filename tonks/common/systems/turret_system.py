import math

import pygame
import esper

from tonks.common.components import Position, Turret

class TurretSystem(esper.Processor):
    def process(self, _dt: float):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for _ent, (pos, turret) in esper.get_components(Position, Turret):
            target_angle = math.atan2(mouse_y - pos.y, mouse_x - pos.x)
            diff = (target_angle - turret.angle + math.pi) % (2 * math.pi) - math.pi
            turret.angle += diff * turret.lag
