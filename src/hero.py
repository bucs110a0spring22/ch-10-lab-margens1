import pygame
import random
#model
class Hero(pygame.sprite.Sprite):
    
    def __init__(self, name, x, y, img_file):
      '''
      initiates the hero class
      args: self, name, x coordinate, y coordinate, image file
      return: initiated version of the class Hero
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
        self.name = name
        self.speed = 3
        self.health = 3

    #methods to make moving our hero easier
    def move_up(self):
        self.rect.y -= self.speed
    def move_down(self):
        self.rect.y += self.speed
    def move_left(self):
        self.rect.x -= self.speed
    def move_right(self):
        self.rect.x += self.speed

    def fight(self, opponent):
      '''
      removes health from the hero when the attack is successful
      args: self, opponent
      return: true or false based of the success of the attack
      '''
        if(random.randrange(3)):
            self.health -= 1
            print("attack failed. Remaining Health: ", self.health)
            return False
        else:
            print("successful attack")
        return True
