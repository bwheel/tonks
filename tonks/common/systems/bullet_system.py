
import math
import esper

from tonks.common.components import Bullet, Position, Velocity


class BulletSystem(esper.Processor):
    def process(self, dt):
        for ent, (pos, vel, bullet) in esper.get_components(Position, Velocity, Bullet):
            pos.x += math.cos(vel.angle) * vel.speed * dt
            pos.y += math.sin(vel.angle) * vel.speed * dt
            bullet.lifetime -= dt
            if bullet.lifetime <= 0:
                esper.delete_entity(ent)
