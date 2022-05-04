import pygame
import random
#model
class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        '''
        initiates the enemy class
        args: self, name, x coordinate, y coordinate, image file
        return: initiated version of the class enemy
        '''
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)

        #The following two attributes must be called image and rect
        #pygame assumes you have intitialized these values
        #and uses them to update the screen

        #create surface object image
        self.image = pygame.image.load(img_file).convert_alpha()
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #set other attributes
        self.name = name + str(id(self))
        self.speed = 1

    def update(self):
      '''
      makes the enemies "wiggle" around by costantly changing their postions by +-1 
      args: self
      return: Moved x and y coordinates
      '''
      self.rect.x += random.randint(-1, 1)
      self.rect.y += random.randint(-1, 1)
      #print(self.rect.x)
      #print(self.rect.y)
      ##print("'Update me,' says " + self.name)
