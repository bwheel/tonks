import math

import pygame
import esper

from tonks.common.components import Bullet, Position, Renderable


class RenderBulletSystem(esper.Processor):
    def __init__(self, screen):
        self.screen = screen

    def process(self, _dt):
        for _ent, (pos, rend, _bullet) in esper.get_components(Position, Renderable, Bullet):
            pygame.draw.circle(self.screen, rend.color, (int(pos.x), int(pos.y)), 3)

