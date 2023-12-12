import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Load Alien Image and set is rect
        original_image = pygame.image.load('resource/alien.bmp')
        self.image = pygame.transform.scale(original_image, (50, 50))
        self.rect = self.image.get_rect()


        #Start each new alien near the top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the alien exact position
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edge(self):
        """Return True if alien is at egde of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <=0:
            return True

    def update(self):
        """ Move the alien right."""
        self.x  += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x  = self.x

    
        



    

