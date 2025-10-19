import math

import pygame
import esper

from tonks.common import constants
from tonks.common.components import Position, Velocity, Turret, Renderable

class RenderTankSystem(esper.Processor):
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

    def process(self, dt: float):
        for _ent, (pos, vel, turret, rend) in esper.get_components(Position, Velocity, Turret, Renderable):
            w, h = rend.size
            points = [
                (-w / 2, -h / 2),
                (w / 2, -h / 2),
                (w / 2, h / 2),
                (-w / 2, h / 2),
            ]
            rotated = []
            for x, y in points:
                rx = x * math.cos(vel.angle) - y * math.sin(vel.angle)
                ry = x * math.sin(vel.angle) + y * math.cos(vel.angle)
                rotated.append((pos.x + rx, pos.y + ry))

            pygame.draw.polygon(self.screen, rend.color, rotated)

            # --- Draw turret ---
            pygame.draw.circle(self.screen, constants.PLAYER_TURRET_COLOR, (int(pos.x), int(pos.y)), 14)

            # --- Draw barrel ---
            barrel_length = 30
            bx = pos.x + math.cos(turret.angle) * barrel_length
            by = pos.y + math.sin(turret.angle) * barrel_length
            pygame.draw.line(self.screen, constants.PLAYER_TURRET_COLOR, (pos.x, pos.y), (bx, by), 5)
