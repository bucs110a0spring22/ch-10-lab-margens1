import sys
import pygame
from pygame.locals import *
import random
from src import hero
from src import enemy


class Controller:
    def __init__(self, width=1280, height=960):
      '''
      initiates the settings of the game
      args: self, width, height
      return: initiated version of the class 
      '''
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
      
        self.backgroundfile = "assets/CH10Background3.jpg"
        #this creates a Surface object - shorcut library
        self.background = pygame.image.load(self.backgroundfile).convert_alpha() 

        self.background = pygame.transform.scale(self.background, (self.width, self.height))

        pygame.font.init()  # you have to call this at the start, if you want to use this module.
        pygame.key.set_repeat(1, 50)  # initialize a held keey to act as repeated key strikes
        """Load the sprites that we need"""

        self.enemies = pygame.sprite.Group()
        num_enemies = 3
        for i in range(num_enemies):
            x = random.randrange(100, 400)
            y = random.randrange(100, 400)
            self.enemies.add(enemy.Enemy("Boogie", x, y, 'assets/enemy.png'))
        self.hero = hero.Hero("Conan", 50, 80, "assets/hero.png")
        self.all_sprites = pygame.sprite.Group((self.hero,) + tuple(self.enemies))
        self.state = "GAME"

    def mainLoop(self):
      '''
      Checks the state of the game
      args: self
      return: goes to game loop depending on the state of the game 
      '''
        while True:
            if(self.state == "GAME"):
                self.gameLoop()
            elif(self.state == "GAMEOVER"):
                self.gameOver()

    def gameLoop(self):
      '''
      runs the game portion of the program
      args: self
      return: functions for hero character
      '''
        while self.state == "GAME":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_UP):
                        self.hero.move_up()
                    elif(event.key == pygame.K_DOWN):
                        self.hero.move_down()
                    elif(event.key == pygame.K_LEFT):
                        self.hero.move_left()
                    elif(event.key == pygame.K_RIGHT):
                        self.hero.move_right()

            # check for collisions
            fights = pygame.sprite.spritecollide(self.hero, self.enemies, True)
            if(fights):
                for e in fights:
                    if(self.hero.fight(e)):
                        e.kill()
                        self.background.fill((250, 250, 250))
                    else:
                        self.background.fill((250, 0, 0))
                        self.enemies.add(e)

            # redraw the entire screen
            self.enemies.update()
            #You have to blit the background every time
            self.screen.blit(self.background, (-150,-500) )
            if(self.hero.health == 0):
                self.state = "GAMEOVER"
            self.all_sprites.draw(self.screen)

            # update the screen
            pygame.display.flip()

    def gameOver(self):
        '''
        sets the game over GUI
        args: self
        return: GUI for when user has lost
        '''
        self.hero.kill()
        myfont = pygame.font.SysFont(None, 30)
        message = myfont.render('Game Over', False, (0, 0, 0))
        self.screen.blit(message, (self.width / 2, self.height / 2))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
