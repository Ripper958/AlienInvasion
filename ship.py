"""ship module"""
import pygame


class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Intialize the ship and its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        #capture settings from ai_game
        self.settings = ai_game.settings

        # load the image and get its rect.
        self.image = pygame.image.load('images/spaceship.bmp')
        self.image_rect = self.image.get_rect()
        # start each new ship at the bottom center of the screen
        self.image_rect.midbottom = self.screen_rect.midbottom
        #Movement flag
        self.moving_right = False
        self.moving_left = False
        #store a decimal value for the ship's horizontal position
        self.x_pos = float(self.image_rect.x)

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.image_rect.right < self.screen_rect.right:
            self.x_pos += self.settings.ship_speed
        if self.moving_left and self.image_rect.left > 0:
            self.x_pos -= self.settings.ship_speed
        #update rect object from self.x
        self.image_rect.x = self.x_pos

    def draw_ship(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.image_rect)
