import enum
import os
from enum import Enum

import pygame.surface


class Phase(Enum):

    NORMAL = enum.auto()
    SPLINTER = enum.auto()


class Size(Enum):

    NORMAL = 32
    SPLINTER = 16

class XSpeed(Enum):

    NORMAL = 3
    SPLINTER = 3


class YSpeed(Enum):

    NORMAL = 0.35
    SPLINTER = 8

class Player:

    def __init__(self, game):

        self.game = game

        self.x = 100 # pos
        self.y = 500
        self.xsm = 1 # speed multiplier
        self.ysm = 1
        self.xv = 1 # velocity
        self.yv = 0

        self.phase: Phase = Phase.SPLINTER
        self.size = Size[self.phase.name.upper()].value

        self.textures = {}

        for p in Phase:
            self.textures[p.name] = (pygame.image.load(os.path.join("assets", "player", str(p.name).lower() + '.bmp')))

        self.jump_timer = -1

        self.gy = (600 - self.size)


    def handle_input(self, keys):

        if keys[pygame.K_SPACE] or keys[pygame.K_RETURN]:
            self.jump()

    def get_speeds(self):
        fxs = XSpeed[self.phase.name.upper()].value
        fys = YSpeed[self.phase.name.upper()].value

        return fxs, fys


    def update(self):

        if self.x > 1000:
            self.x = 0

        self.size = Size[self.phase.name.upper()].value
        cy = (0 + self.size) # platform
        gy = (600 - self.size) # ground

        fxs = self.get_speeds()[0]
        fys = self.get_speeds()[1]

        self.xv = (fxs * self.xsm)

        if self.phase == Phase.NORMAL:
            self.yv += (fys * self.ysm)
        elif self.phase == Phase.SPLINTER:
            self.yv = (fys * self.ysm)

        self.x += self.xv
        self.y += self.yv

        if self.y >= gy:
            self.y = gy

        if self.y <= cy:
            self.y = cy

        print("y:", self.y)
        print("vy:", self.yv)

        self.game.breadcrumbs.append([
            self.x,
            self.y
        ])

    def jump(self):

        if self.phase == Phase.SPLINTER:
            self.y -= self.get_speeds()[1] * 2

        if self.jump_timer >= 0:
            self.jump_timer = -1
            return

        if self.phase == Phase.NORMAL:
            if self.y >= self.gy:
                self.yv = -8

    def render(self, screen: pygame.surface.Surface):
        screen.blit(self.textures[self.phase.name], (self.x, self.y))


# class PlayerBase:
#
#     def __init__(self):
#         pass