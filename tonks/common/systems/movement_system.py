import math

import pygame
import esper

from tonks.common.components import TankControl, Position, Velocity

class MovementSystem(esper.Processor):
    def process(self, dt: float):
        keys = pygame.key.get_pressed()
        for _ent, (pos, vel, ctrl) in esper.get_components(Position, Velocity, TankControl):
            if keys[pygame.K_a]:
                vel.angle -= ctrl.turn_speed * dt
            if keys[pygame.K_d]:
                vel.angle += ctrl.turn_speed * dt

            move_dir = 0
            if keys[pygame.K_w]:
                move_dir += 1
            if keys[pygame.K_s]:
                move_dir -= 1

            if move_dir != 0:
                speed = ctrl.forward_speed if move_dir > 0 else ctrl.backward_speed
                pos.x += math.cos(vel.angle) * speed * dt * move_dir
                pos.y += math.sin(vel.angle) * speed * dt * move_dir
