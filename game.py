import pygame

import player


class Game:

    def __init__(self):

        self.run = True

        self.screen = pygame.display.set_mode((1000, 600), pygame.RESIZABLE)

        self.player = player.Player(self)

        self.camera = [0, 0]
        self.breadcrumbs = []


    def update(self, events: list[pygame.event.Event]):

        self.player.update()

        for event in events:
            if event.type == pygame.KEYDOWN:
                pass

        keys = pygame.key.get_pressed()

        self.player.handle_input(keys)

        return self.run

    def draw(self):

        screen = self.screen
        screen.fill((0, 0, 0))

        self.camera[0] += 1

        self.breadcrumbs = self.breadcrumbs[-50:]

        for coord in self.breadcrumbs:
            pygame.draw.circle(screen, (255, 255, 255), (int(coord[0]), int(coord[1])), 2)

        self.player.render(screen)

        pygame.display.update()