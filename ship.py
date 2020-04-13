"""ship module"""
import pygame


class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Intialize the ship and its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load the image and get its rect.
        self.image = pygame.image.load('images/spaceship.png')
        self.image_rect = self.image.get_rect()
        # start each new ship at the bottom center of the screen
        self.image_rect.midbottom = self.screen_rect.midbottom

    def draw_ship(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.image_rect)
