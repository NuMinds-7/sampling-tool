import pygame

from app_handler import *
from display_handler import *
from event_handler import *


class Tool:
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()

        pygame.display.set_caption('Sample Retrieval Tool')
        pygame.display.set_icon(pygame.image.load('assets/icon.png'))
        self.screen = pygame.display.set_mode(WINDOW_SIZE)

        self.app_handler = AppHandler()
        self.display_handler = DisplayHandler(self.app_handler)
        self.event_handler = EventHandler(self.app_handler)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.app_handler.set_state('QUIT')
                elif event.type == pygame.KEYDOWN:
                    self.event_handler.update_key(event.key)

            self.app_handler.update()
            self.display_handler.update(self.screen)

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    tool = Tool()
    tool.run()
