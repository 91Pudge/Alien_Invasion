

import sys


import pygame

from pygame.sprite import Group

from ship import Ship

from settings import Settings

from game_stats import GameStats

from button import Button

from alien import Alien

import game_functions as gf



def run_game():
    #Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")


    # make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    #create an instance to store game statistics.
    stats = GameStats(ai_settings)

    #make a ship
    ship = Ship(ai_settings, screen)

    #make a group to store bulllets in.
    bullets = Group()
    aliens = Group()

   

    #set set the background color
    bg_color = (0, 0, 255)

    

     #Create the fleet of aleins.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Make an Alien
    alien = Alien(ai_settings, screen)


    #start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, play_button)
        #make the most recently drawn screen visible
        pygame.display.flip()

        
        

        


        


run_game()
