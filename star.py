import numpy as np

import pygame

class Stars():
    """position, size of stars and function drawing stars"""
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def draw_stars(self, screen):
        """draw stars using a loop"""
        for i in range(40):
            pygame.draw.circle(screen, (255, 255, 255), (self.x[i], self.y[i]), self.r[i])


def stars_position(ll_settings):
    """get random position of x and y and size for stars"""
    x = np.random.random_integers(0, ll_settings.screen_width, size=40)
    y = np.random.random_integers(0, ll_settings.screen_height - ll_settings.ground_height,\
        size=40)
    #get random radius values
    r = np.random.random_integers(0, 5, size=40)
    return x, y, r
