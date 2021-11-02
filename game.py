import sys

import pygame

from ship import Lander
import game_functions as gf
import star
from star import Stars
import stats

class Settings():
    """settings of window and background"""

    def __init__(self, screen_width, screen_height, bg_color, ground_height, g_color):
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.bg_color = bg_color
        self.ground_height = ground_height
        self.g_color = g_color

class GameSetup():
    """storing initial physical values and constantsas well as some limitting values"""
    def __init__(self, height, velocity, gravity, acceleration, max_acc, acc_speed, \
        max_speed, dt, fuel, fuel_rate):
        self.height = height
        self.velocity = velocity
        self.gravity = gravity
        self.dt = dt
        self.acceleration = acceleration #initial acceleration value
        self.max_acc = max_acc #maximum acceleration
        self.acc_speed = acc_speed #speed with which acceleration is controlled
        self.max_speed = max_speed #max speed to land safely
        self.fuel = fuel
        self.fuel_rate = fuel_rate

def run_game(height, gravity, velocity, fuel):
    """main function running the game"""
    #initialize game and create screen
    pygame.init()

    #initialize screen settings
    ll_settings = Settings(1200, 600, (0, 0, 102), 100, (129, 129, 129))

    #window/ screen settings
    screen = pygame.display.set_mode((ll_settings.screen_width, ll_settings.screen_height))
    pygame.display.set_caption('Lunar Lander')

    #initial values of the game
    setup = GameSetup(height, 0, gravity, 1, 5, 0.15, velocity, 0.01, fuel, 0.03)
    #initialize lander class
    lander = Lander(screen, ll_settings, setup)

    #initialize stars class
    x, y, r = star.stars_position(ll_settings)
    stars = Stars(x, y, r)

    #main loop of the game
    while True:

        #background
        screen.fill(ll_settings.bg_color)
        ground = pygame.draw.rect(screen, ll_settings.g_color, (0, ll_settings.screen_height - ll_settings.ground_height,
            ll_settings.screen_width, ll_settings.ground_height))
        #drawing stars
        stars.draw_stars(screen)
        #displaying max velocity
        stats.velocity_reminder(screen, setup)

        gf.check_events(lander, setup)
        gf.update_screen(lander, setup, screen)

        lander.land_check(ll_settings)

        #redraw screen
        pygame.display.flip()
