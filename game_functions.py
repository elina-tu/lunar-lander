import pygame

import sys

import stats

def update_screen(lander, setup, screen):
    """draw/update everything on screen"""
    #updating lander position
    if lander.landed == False:
        #set engine off when you run out of fuel
        if lander.fuel <= 0:
            lander.acceleration = 0
            #set fuel to zero so it doesnt display slightly negative value
            lander.fuel = 0
        #calcuating velocity and position
        lander.velocity += (setup.gravity + lander.acceleration) * setup.dt
        lander.phys_height += lander.velocity * setup.dt
        #fuel decrease
        lander.fuel -= setup.fuel_rate*lander.acceleration

        #update position
        lander.pix_height -= lander.velocity * setup.dt * lander.pixpermeter
        lander.rect.bottom = lander.pix_height
    #display win screen
    elif abs(lander.velocity) < setup.max_speed:
        win_sceen(screen)
    #display loose screen
    else:
        lose_sceen(screen)

    #displaying stats
    stats.display_height(screen, lander)
    stats.display_velocity(screen, lander)
    stats.display_acceleration(screen, lander)
    stats.fuel_bar(screen, lander, setup)

    #drawing lander
    lander.blitme()

def check_events(lander, setup):
    """Register and respond to mouse and keyboard input"""
    for event in pygame.event.get():
        #close
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            #set engines on
            if event.key == pygame.K_SPACE:
                if lander.fuel > 0:
                    lander.engine = True
                    lander.acceleration = setup.acceleration
            #increase acceleration by pressing up arrow key
            elif event.key == pygame.K_UP:
                if lander.engine & (lander.acceleration < setup.max_acc):
                    lander.acceleration += setup.acc_speed
            #decrease acceleration by pressing down arrow key
            elif event.key == pygame.K_DOWN:
                if lander.engine & (lander.acceleration > 0):
                    lander.acceleration -= setup.acc_speed

        #engine turns off
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                lander.engine = False
                lander.acceleration = 0

def win_sceen(screen):
    """Create and display text after victory"""
    #creating text and selecting font
    font = pygame.font.SysFont('calibri', size=25)
    text = font.render('Congratulations! You landed safely.', True, (255, 255, 255))

    #position text
    textRect = text.get_rect()
    screen_rect = screen.get_rect()
    textRect.centerx = screen_rect.centerx
    textRect.centery = screen_rect.centery
    screen.blit(text, textRect)

def lose_sceen(screen):
    """Create and display text after victory"""
    #creating text and selecting font
    font = pygame.font.SysFont('calibri', size=25)
    text = font.render('You crashed :(', True, (255, 255, 255))

    #position text
    textRect = text.get_rect()
    screen_rect = screen.get_rect()
    textRect.centerx = screen_rect.centerx
    textRect.centery = screen_rect.centery

    #draw onto the screen
    screen.blit(text, textRect)
