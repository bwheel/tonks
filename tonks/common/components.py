from dataclasses import dataclass as component
from typing import Tuple, Union

@component
class Position():
  x: float
  y: float

@component
class Velocity:
    speed: float = 0.0
    angle: float = 0.0  # facing direction in radians

@component
class Rotation:
    rotation_speed: float = 0.0

@component
class TankControl:
    forward_speed: float = 150.0
    backward_speed: float = 100.0
    turn_speed: float = 2.0  # radians/sec

@component
class Turret:
    angle: float = 0.0
    lag: float = 0.1  # how slow it follows the mouse

@component
class Renderable:
    color: tuple[int, int, int] # r,g,b
    size: tuple[int, int]  # width, height

@component
class Weapon:
    cooldown: float = 0.3
    timer: float = 0.0
    bullet_speed: float = 500.0

@component
class Bullet:
    lifetime: float = 2.0
