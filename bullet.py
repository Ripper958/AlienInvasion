"Module to manage bullets fired from the ship"""
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):
        """Create a bullter object at the ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create a bullter rect at (0, 0) and then set the correct position
        self.bullet_rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                       self.settings.bullet_height)
        self.bullet_rect.midtop = ai_game.ship.image_rect.midtop

        # store the bullet's position as a decimal value
        self.pos_y = float(self.bullet_rect.y)

    def update(self):
        """Move the bullet up the screen"""
        # update the decimal position of the bullet
        self.pos_y -= self.settings.bullet_speed
        # update the bullet rect position
        self.bullet_rect.y = self.pos_y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.bullet_rect)
