import pygame
import sys

class Lander():
    """describes lunar lander"""
    def __init__(self, screen, ll_settings, setup):
        #sreen surface
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        #ship image
        self.image = pygame.image.load('lander.bmp')
        self.rect = self.image.get_rect()

        # set initial ship position
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = 1/5 * ll_settings.screen_height
        #define a float to move by non integer number of pixels
        self.pix_height = float(self.rect.bottom)

        #ship has landed?
        self.landed = False
        #current acceleration of the ship
        self.acceleration = 0
        #engine on
        self.engine = False
        self.fuel = setup.fuel

        #pixels per meter
        self.pixpermeter = ((ll_settings.screen_height - ll_settings.ground_height)\
            - self.rect.bottom) / setup.height

        #inital position, velocity parameters
        self.velocity = setup.velocity
        self.phys_height = setup.height

    def blitme(self):
        '''draw lander on screen'''
        self.screen.blit(self.image, self.rect)

    def land_check(self, ll_settings):
        """check if ship landed"""
        if self.rect.bottom >= ll_settings.screen_height - ll_settings.ground_height:
            self.landed = True
