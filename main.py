import pygame
from src.controller import Controller
#import your controller

def main():
    pygame.init()
    #Create an instance on your controller object
    pong_game = Controller()
    #Call your mainloop
    pong_game.mainloop()
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
