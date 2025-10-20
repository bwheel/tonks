import pathlib

import esper
import pygame

from tonks.common.components import  Position,  Turret, Weapon
from tonks.common.entities import spawn_bullet

POO_SOUND_FILE_PATH = pathlib.Path("assets", "sfx", "byron-voice-poo-1.wav")

class WeaponSystem(esper.Processor):
    def __init__(self):
        self.poo_sound = pygame.mixer.Sound(POO_SOUND_FILE_PATH.absolute())
        super().__init__()
    def process(self, dt):
        mouse_pressed = pygame.mouse.get_pressed()[0]  # 0 = left button
        for _ent, (pos, turret, weapon) in esper.get_components(Position, Turret, Weapon):
            weapon.timer -= dt
            if mouse_pressed and weapon.timer <= 0:
                weapon.timer = weapon.cooldown
                spawn_bullet(pos, turret, weapon)
                self.poo_sound.play()
