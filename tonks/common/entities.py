import math
import pygame
import esper

from tonks.common import constants
from tonks.common.components import Bullet, Position, Renderable, TankControl, Turret, Velocity, Weapon


def spawn_player(x: float, y: float, color = constants.PLAYER_COLOR):
    player = esper.create_entity()
    esper.add_component(player, Position(x, y))
    esper.add_component(player, Velocity())
    esper.add_component(player, TankControl())
    esper.add_component(player, Weapon(cooldown=0.3))
    esper.add_component(player, Turret(lag=0.1))
    esper.add_component(player, Renderable(color=color, size=(60, 40)))
    return player


def spawn_bullet(pos, turret, weapon):
    # spawn position: tip of barrel
    barrel_length = 30
    bx = pos.x + math.cos(turret.angle) * barrel_length
    by = pos.y + math.sin(turret.angle) * barrel_length

    bullet_speed = weapon.bullet_speed
    vx = math.cos(turret.angle) * bullet_speed
    vy = math.sin(turret.angle) * bullet_speed

    bullet = esper.create_entity()
    esper.add_component(bullet, Position(bx, by))
    esper.add_component(bullet, Velocity(angle=turret.angle, speed=bullet_speed))
    esper.add_component(bullet, Bullet(lifetime=2.0))
    esper.add_component(bullet, Renderable(constants.BULLET_COLOR, (6, 6)))
